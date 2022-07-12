import logging
from itertools import chain
from typing import *

from .FeatureSet import FeatureSet
from .rawuta import RawUTA


class UTA:
    logger = logging.getLogger(__name__)

    def __init__(self, features: List[FeatureSet], same_tier_is_equivalent=False):
        self.features = features
        raw_features = list(chain(*[[(f.n, f.worst, f.best) for f in fset.descriptors] for fset in self.features]))
        self.uta = RawUTA(raw_features, same_tier_is_equivalent=same_tier_is_equivalent)

    def add(self, reference_ranking: List[Collection[str]]):
        variants = list(set(chain(*reference_ranking)))
        batch_features = [f.compute_batch(variants) for f in self.features]
        raw_features = {variant: list(chain(*[f[i] for f in batch_features])) for i, variant in enumerate(variants)}
        self.uta.add(reference_ranking, raw_features)

    def solve(self):
        return self.uta.solve()

    def U(self, variants: Union[List[str], str]) -> Union[List[float], float]:
        singular = isinstance(variants, str)
        if singular:
            variants = [variants]
        batch_features = [f.compute_batch(variants) for f in self.features]
        result = [self.uta.U(chain(*[f[i] for f in batch_features])).value for i in range(len(variants))]
        return result[0] if singular else result
