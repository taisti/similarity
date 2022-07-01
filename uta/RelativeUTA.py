from typing import *

from .FeatureSet import FeatureDescriptor, FeatureSet
from .uta import UTA


class RelativeFeatureSet(FeatureSet):
    def __init__(self, base: FeatureSet):
        self.base = base
        self.descriptors = [
            FeatureDescriptor(f"Absolute value of the difference on {d.name}", best=0, worst=abs(d.worst - d.best),
                              n=d.n) for d in base.descriptors]
        self.reference = None

    def compute(self, id: str) -> List[float]:
        assert self.reference is not None
        reference = self.base.compute(self.reference)
        current = self.base.compute(id)
        values = [abs(r - c) for r, c in zip(reference, current)]
        return values


class RelativeUTA:
    def __init__(self, features: List[FeatureSet]):
        self.uta = UTA(features)

    def add(self, reference: str, better: List[str], worse: List[str]):
        for f in self.uta.features:
            if isinstance(f, RelativeFeatureSet):
                f.reference = reference
        self.uta.add([better, worse])

    def U(self, reference: str, variants: Union[List[str], str]) -> Union[List[float], float]:
        for f in self.uta.features:
            if isinstance(f, RelativeFeatureSet):
                f.reference = reference
        return self.uta.U(variants)

    def recommend(self, reference: Any, variants: List[Any]) -> Tuple[Any, float]:
        scores = self.U(reference, variants)
        i = max(range(len(scores)), key=scores.__getitem__)
        return variants[i], scores[i]

    def solve(self):
        self.uta.solve()
