import gzip
import json
import logging
import zipfile
from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import *

import requests
from tqdm import tqdm

from helpers import NamedClass
from uta import FeatureSet, FeatureDescriptor


def _download(target: Path, url: str, expected_size: Optional[int]):
    if target.exists() and target.stat().st_size == expected_size:
        return
    r = requests.get(url, stream=True)
    with target.open('wb') as f:
        for chunk in tqdm(r.iter_content(chunk_size=1024 * 1024)):
            f.write(chunk)


def _load(path: Path):
    with zipfile.ZipFile(path) as zipf:
        names = zipf.namelist()
        assert len(names) == 1
        with zipf.open(names[0]) as f:
            data = json.load(f)
    assert hasattr(data, "values") and len(data.values()) == 1
    data = next(iter(data.values()))
    return {row["fdcId"]: row for row in tqdm(data)}


def _load_mapping(path: Path) -> Dict[str, List[int]]:
    result = defaultdict(list)
    with path.open('rt') as f:
        for row in f.readlines():
            row = row.strip()
            if len(row) == 0 or row[0] == '#':
                continue
            row = row.split()
            if len(row) < 2:
                continue
            fdcid, foodon = row[:2]
            fdcid = int(fdcid)
            if '/' not in foodon:
                foodon = 'http://purl.obolibrary.org/obo/' + foodon
            result[foodon].append(fdcid)
    return result


def _load_fdc(cache_dir: Path):
    gbf_path = cache_dir / 'FoodData_Central_branded_food_json_2022-04-28.zip'
    _download(gbf_path,
              'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_json_2022-04-28.zip',
              167202939)
    data = _load(gbf_path)
    ff_path = cache_dir / 'FoodData_Central_foundation_food_json_2022-04-28.zip'
    _download(ff_path,
              'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_json_2022-04-28.zip',
              335596)
    data.update(_load(ff_path))
    return data


class FDC:
    mapped: Dict[str, List[Mapping]] = None

    @classmethod
    def _prepare(cls, cache_dir: Path):
        cache_dir.mkdir(parents=True, exist_ok=True)

        mapping_paths = [Path("fdc2foodon-auto.tsv"), Path("fdc2foodon.tsv")]

        mapping = {}
        for mapping_path in mapping_paths:
            mapping.update(_load_mapping(mapping_path))
        mapped_cache_file = cache_dir / 'mapped.json.gz'
        if mapped_cache_file.exists() and \
                all(mp.stat().st_mtime <= mapped_cache_file.stat().st_mtime for mp in mapping_paths):
            with gzip.open(mapped_cache_file, 'rt') as f:
                mapped = json.load(f)
        else:
            fdc = _load_fdc(cache_dir)
            mapped = {k: [fdc[v] for v in ids] for k, ids in mapping.items()}
            with gzip.open(mapped_cache_file, 'wt') as f:
                json.dump(mapped, f)
        cls.mapped = mapped

    def __init__(self):
        if FDC.mapped is None:
            FDC._prepare(Path("cache/FDC"))

    def __getitem__(self, item: Union[str, NamedClass]) -> List[Mapping]:
        if hasattr(item, 'iri'):
            item = item.iri
        return FDC.mapped[item]


class FDCFeatureSet(FeatureSet):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.fdc = FDC()
        _features = [
            ({'208', '957', '958'}, FeatureDescriptor("Energy [kcal]", 1, 1000, 0)),
            ({'203'}, FeatureDescriptor("Protein [g]", 1, 0, 100)),
            ({'204'}, FeatureDescriptor("Total lipid [g]", 1, 100, 0)),
            ({'307'}, FeatureDescriptor("Sodium [mg]", 1, 100000, 0))
        ]
        self.descriptors = [f[1] for f in _features]
        self._numbers = [f[0] for f in _features]

    def compute(self, id: Union[NamedClass, str]) -> List[float]:
        if hasattr(id, 'iri'):
            id = id.iri

        def extract_nutrient(numbers: Set[str]) -> List[float]:
            result = list(
                chain(*[[n['amount'] for n in item if str(n['nutrient']['number']) in numbers] for item in raw]))
            if len(result) == 0:
                FDCFeatureSet.logger.warning(f"No information for nutrients {numbers} for IRI {id}")
            return result

        def avg(inp: List[float]) -> float:
            if len(inp) == 0:
                return float("nan")
            return sum(inp) / len(inp)

        raw = self.fdc[id]
        raw = [item['foodNutrients'] for item in raw]
        return [avg(extract_nutrient(n)) for n in self._numbers]


def generate_mappings():
    import re
    from helpers import foodon
    r_delim = re.compile(r'[\s,-]')

    cache_dir = Path("cache/FDC")

    names_file = cache_dir / "names.txt.gz"

    if not names_file.exists():
        fdc = _load_fdc(cache_dir)
        with gzip.open(names_file, 'wt') as f:
            for fdcid, item in fdc.items():
                print(fdcid, item["description"], file=f)

    def preprocess(text: str) -> set[str]:
        text = text.lower().strip().replace('(', '').replace(')', '')
        return {s for s in map(str.strip, r_delim.split(text.lower().strip())) if len(s) > 0}

    fdc = {}
    with gzip.open(names_file, 'rt') as f:
        for line in f.readlines():
            fdcid, name = line.strip().split(maxsplit=1)
            fdc[fdcid] = (name, preprocess(name))

    onto = foodon()
    obo = onto.get_namespace("http://purl.obolibrary.org/obo/")

    with open('fdc2foodon-auto.tsv', 'wt') as f:
        for cls in tqdm(obo.FOODON_00001002.descendants()):
            for label in cls.label:
                b = preprocess(label)
                for fdcid, (name, a) in fdc.items():
                    if a == b:
                        print(fdcid, cls.iri, name, "->", label, file=f)


if __name__ == '__main__':
    generate_mappings()
