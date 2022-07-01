from dataclasses import dataclass
from typing import List, Dict, Sequence, Any


@dataclass
class FeatureDescriptor:
    name: str
    n: int
    worst: float
    best: float


class FeatureSet:
    descriptors: List[FeatureDescriptor]

    def compute(self, id: Any) -> List[float]:
        raise NotImplemented()

    def compute_batch(self, ids: List[Any]) -> List[List[float]]:
        return list(map(self.compute, ids))


class DictFeatureSet(FeatureSet):
    def __init__(self, data: Dict[str, Sequence[float]], descriptors: List[FeatureDescriptor]):
        self.data = data
        self.descriptors = descriptors

    def compute(self, id: str) -> Sequence[float]:
        return self.data[id]
