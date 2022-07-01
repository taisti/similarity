import logging
from typing import List, Any

from rdflib.plugins.sparql import prepareQuery

from uta.FeatureSet import FeatureSet, FeatureDescriptor
from WikiFCD import WikiFCD


class WikiFCDFeatureSet(FeatureSet):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self._wikifcd = WikiFCD()
        _features = [
            (
                "?item p:P6/psv:P6 [wikibase:quantityAmount ?amount; wikibase:quantityUnit <http://wikifcd.wiki.opencura.com/entity/Q11> ] ",
                FeatureDescriptor("Energy [kcal]", 1, 1000, 0)
            ),
            (
                "?item p:P7/psv:P7 [wikibase:quantityAmount ?amount; wikibase:quantityUnit <http://wikifcd.wiki.opencura.com/entity/Q8> ] ",
                FeatureDescriptor("Protein [g]", 1, 0, 100)
            ),
            (
                "?item p:P8/psv:P8 [wikibase:quantityAmount ?amount; wikibase:quantityUnit <http://wikifcd.wiki.opencura.com/entity/Q8> ] ",
                FeatureDescriptor("Total lipid [g]", 1, 100, 0)
            ),
            # (
            #     "?item p:P88/psv:P88 [wikibase:quantityAmount ?amount; wikibase:quantityUnit <http://wikifcd.wiki.opencura.com/entity/Q8> ] ",
            #     FeatureDescriptor("Fatty acids, total polyunsaturated [g]", 1, 0, 100)
            # ),
        ]
        _template = """
            PREFIX wd: <http://www.wikidata.org/entity/>
            PREFIX wbt: <http://wikifcd.wiki.opencura.com/prop/direct/>
            PREFIX wb: <http://wikifcd.wiki.opencura.com/entity/>
            prefix p: <http://wikifcd.wiki.opencura.com/prop/>
            prefix ps: <http://wikifcd.wiki.opencura.com/prop/statement/>
            prefix psv: <http://wikifcd.wiki.opencura.com/prop/statement/value/>
            prefix wikibase: <http://wikiba.se/ontology#>

            SELECT ?amount WHERE {$body}
                """
        self._queries = [prepareQuery(_template.replace("$body", f[0])) for f in _features]
        self._descriptors = [f[1] for f in _features]

    @property
    def descriptors(self) -> List[FeatureDescriptor]:
        return self._descriptors

    def compute(self, id: Any) -> List[float]:
        if hasattr(id, 'iri'):
            id = id.iri
        g = self._wikifcd[id]
        if g is None:
            return [d.worst for d in self._descriptors]
        item, g = g
        result = []
        for descriptor, q in zip(self._descriptors, self._queries):
            rows = list(g.query(q, initBindings={"item": item}))
            assert len(rows) <= 1
            if len(rows) == 1:
                assert len(rows[0]) == 1
                value = float(rows[0][0])
            else:
                self.logger.warning(
                    f"While computing the features for {id}, the query for {descriptor.name} returned no results. "
                    f"Assuming the worst value of {descriptor.worst}.")
                value = descriptor.worst
            result.append(value)
        return result


if __name__ == '__main__':
    fs = WikiFCDFeatureSet()
    fs.compute('http://purl.obolibrary.org/obo/FOODON_03304999')
