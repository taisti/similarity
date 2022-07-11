from itertools import chain
from typing import *

from helpers import is_subclass, textual, ClassExpression
from uta import FeatureSet, FeatureDescriptor


class OWLReadyClassMembershipFeatureSet(FeatureSet):
    def __init__(self, positive_classes: Sequence[ClassExpression], negative_classes: Sequence[ClassExpression]):
        self.positive_classes = positive_classes
        self.negative_classes = negative_classes
        self._descriptors = \
            [FeatureDescriptor("Belongs to " + textual(c), 1, 0.0, 1.0) for c in self.positive_classes] + \
            [FeatureDescriptor("Belongs to " + textual(c), 1, 1.0, 0.0) for c in self.negative_classes]

    @property
    def descriptors(self) -> List[FeatureDescriptor]:
        return self._descriptors

    def compute(self, e: ClassExpression):
        return [1.0 if is_subclass(e, s) else 0.0 for s in chain(self.positive_classes, self.negative_classes)]
