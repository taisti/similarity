import bisect
from dataclasses import dataclass
from typing import List

import cvxpy as cp
from cvxpy.constraints import NonNeg


@dataclass
class LinearPiece:
    start: float
    endExclusive: float
    a: float
    b: float


class PiecewiseLinear:
    def __init__(self, n: int, worst: float, best: float):
        self.n = n
        self.worst = worst
        self.best = best
        if worst < best:
            self.is_max = True
        else:
            self.is_max = False
            worst = -worst
            best = -best
        self.weights = cp.Variable(n + 1)
        self.points = [i / n * (best - worst) + worst for i in range(self.n + 1)]

    def expr(self, x: float):
        if not self.is_max:
            assert self.best <= x <= self.worst, f"{self.best} <= {x} <= {self.worst}"
            x = -x
        else:
            assert self.worst <= x <= self.best, f"{self.worst} <= {x} <= {self.best}"
        i = bisect.bisect_left(self.points, x) - 1
        if i < 0:
            return self.weights[0]
        s = [self.weights[i + 1] * (x - self.points[i])]
        for j in range(i, 0, -1):
            s += [self.weights[j] * (self.points[j] - self.points[j - 1])]
        s += [self.weights[0]]
        return sum(s)

    def constraints(self) -> List[NonNeg]:
        return [NonNeg(w) for w in self.weights]
