import json
from pathlib import Path
from typing import Optional, Tuple

import rdflib
import requests
from rdflib import URIRef


class WikiFCD:

    def __init__(self):
        self.cache_root = Path('wikifcd')
        self.cache_root.mkdir(parents=True, exist_ok=True)
        assert self.cache_root.is_dir()
        with open('wikifcd2foodon.json', 'rt') as f:
            data = json.load(f)
            self.foodon2wikifcd = {
                'http://purl.obolibrary.org/obo/FOODON_' + row['foodon']['value']: row['item']['value'] for row
                in data['results']['bindings']}
        with open('wikifcd2foodon.tsv', 'rt') as f:
            for row in f.readlines():
                row = row.strip()
                if len(row) == 0 or row[0] == '#':
                    continue
                row = row.split()
                if len(row) < 2:
                    continue
                wikicfd, foodon = row[:2]
                if '/' not in wikicfd and '/' not in foodon and foodon[0] == 'Q':
                    wikicfd, foodon = foodon, wikicfd
                if '/' not in wikicfd:
                    wikicfd = 'http://wikifcd.wiki.opencura.com/entity/' + wikicfd
                if '/' not in foodon:
                    foodon = 'http://purl.obolibrary.org/obo/' + foodon
                self.foodon2wikifcd[foodon] = wikicfd

    def _download(self, iri: str) -> Path:
        # http://wikifcd.wiki.opencura.com/entity/Q239954
        fn = self.cache_root / (iri[iri.rindex('/') + 1:] + ".ttl")
        if not fn.exists():
            # Using Turtle due to https://github.com/RDFLib/rdflib/issues/1050
            r = requests.get(iri, headers={'Accept': 'text/turtle'})
            r.raise_for_status()
            with open(fn, 'wt') as f:
                print(r.text, file=f)
        return fn

    def __getitem__(self, item: str) -> Optional[Tuple[URIRef, rdflib.Graph]]:
        """ Returns a graph from WikiCFD for [item], expected to be a FoodOn IRI, or None if there is no mapping from
        FoodOn IRI to WikiCFD """
        wikifcd_iri = self.foodon2wikifcd[item]
        if wikifcd_iri is None:
            return None
        g = rdflib.Graph()
        g.parse(str(self._download(wikifcd_iri)))
        return URIRef(wikifcd_iri), g


def main():
    wikifcd = WikiFCD()
    print(wikifcd['http://purl.obolibrary.org/obo/FOODON_03301107'])
    print(wikifcd['http://purl.obolibrary.org/obo/FOODON_03304999'])
    # rdflib.Graph().parse('http://wikifcd.wiki.opencura.com/entity/Q562036')


if __name__ == '__main__':
    main()
