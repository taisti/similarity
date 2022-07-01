from itertools import chain
from typing import *

from owlready2 import Ontology

from helpers import is_subclass, textual
from uta import FeatureSet, FeatureDescriptor


class OWLReadyClassMembershipFeatureSet(FeatureSet):
    def __init__(self, onto: Ontology, positive_classes: Iterable[str], negative_classes: Iterable[str]):
        self.onto = onto
        self.positive_classes = positive_classes
        self.negative_classes = negative_classes
        self._descriptors = [FeatureDescriptor("Belongs to " + textual(c), 1, 0.0, 1.0) for c in
                             self.positive_classes] + [FeatureDescriptor("Belongs to " + textual(c), 1, 1.0, 0.0) for c
                                                       in self.negative_classes]

    @property
    def descriptors(self) -> List[FeatureDescriptor]:
        return self._descriptors

    def compute(self, id: Any):
        if isinstance(id, str):
            e = self.onto.search_one(iri=id)
        else:
            e = id
        return [1.0 if is_subclass(e, s) else 0.0 for s in chain(self.positive_classes, self.negative_classes)]
