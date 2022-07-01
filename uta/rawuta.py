from collections import defaultdict
from itertools import chain

import cvxpy as cp

from .PiecewiseLinear import PiecewiseLinear


class RawUTA:
    def __init__(self, features, same_tier_is_equivalent=True):
        self.u = [PiecewiseLinear(*f) for f in features]
        self.constraints = [
            sum(ui.expr(ui.worst) for ui in self.u) == 0,
            sum(ui.expr(ui.best) for ui in self.u) == 1,
        ]
        self.constraints += chain(*[ui.constraints() for ui in self.u])
        self.eps = 1e-5
        self.d = defaultdict(cp.Variable)
        self.same_tier_is_equivalent = same_tier_is_equivalent
        # Regularyzacja nie jest taka oczywista w tym modelu, bo przecież mamy składniki, które czasami wprowadzają stałą, a czasami zmienną wartość
        # self.alpha = None

    def add(self, reference_ranking, variants):
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
        # if self.alpha is not None and self.alpha != 0:
        #     goal += self.alpha * sum([cp.sum(cp.abs(ui.weights[1:])) for ui in self.u])
        goal = cp.Minimize(goal)
        prob = cp.Problem(goal, self.constraints)
        return prob.solve()

    def U(self, xs):
        return sum(ui.expr(x) for x, ui in zip(xs, self.u))
