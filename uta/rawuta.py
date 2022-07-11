from collections import defaultdict
from itertools import chain
from typing import *

import cvxpy as cp

from .PiecewiseLinear import PiecewiseLinear


class RawUTA:
    def __init__(self, features: Sequence[Tuple[int, float, float]], same_tier_is_equivalent=True):
        self.u = [PiecewiseLinear(*f) for f in features]
        self.constraints = [
            sum(ui.expr(ui.worst) for ui in self.u) == 0,
            sum(ui.expr(ui.best) for ui in self.u) == 1,
        ]
        self.constraints += chain(*[ui.constraints() for ui in self.u])
        self.eps = 1e-5
        self.d = defaultdict(cp.Variable)
        self.same_tier_is_equivalent = same_tier_is_equivalent

    def add(self, reference_ranking: Sequence[Collection[Any]], variants: Mapping[Any, Sequence[float]]):
        """
        Be aware that add relies on unique names to identify variants.
        """
        for better, worse in zip(reference_ranking[:-1], reference_ranking[1:]):
            for b in better:
                for w in worse:
                    self.constraints += [self.U(variants[b]) + self.d[b] >= self.U(variants[w]) + self.d[w] + self.eps]
        if self.same_tier_is_equivalent:
            for equivalent in reference_ranking:
                for i, b in enumerate(equivalent):
                    for w in equivalent[i + 1:]:
                        self.constraints += [self.U(variants[b]) + self.d[b] == self.U(variants[w]) + self.d[w]]

    def solve(self):
        goal = sum([cp.abs(v) for v in self.d.values()])
        goal = cp.Minimize(goal)
        prob = cp.Problem(goal, self.constraints)
        return prob.solve()

    def U(self, xs: Iterable[float]) -> cp.Expression:
        return sum(ui.expr(x) for x, ui in zip(xs, self.u))
