import unittest

import cvxpy as cp

from uta import PiecewiseLinear


class PiecewiseLinearTest(unittest.TestCase):
    def test_max_three_pieces(self):
        # 0..90 / 3 pieces -> 0..30, 30..60, 60..90
        # x/2 for 0<=x<30 -> 0<=y<15
        # x/3 + 5 for 30<=x<60 -> 15<=y<25
        # x/6 + 15 for 60<=x<90 -> 25<=y<30
        f = PiecewiseLinear(n=3, worst=0, best=90)
        self.assertListEqual([0, 30, 60, 90], f.points)
        points = [  # (-10, 0),
            (10, 5), (20, 10),
            (33, 16), (51, 22),
            (66, 26), (78, 28),
            # (100, 30)
        ]
        goal = cp.Minimize(sum([cp.abs(f.expr(x) - y) for x, y in points]))
        prob = cp.Problem(goal, f.constraints())
        error = prob.solve()
        self.assertAlmostEqual(0, error)
        for x, y in points:
            self.assertAlmostEqual(y, f.expr(x).value)

    def test_min_three_pieces(self):
        # 0..90 / 3 pieces -> 0..30, 30..60, 60..90
        # -x/2 + 50 for 0<=x<30 -> 50>=y>35
        # -x/3 + 45 for 30<=x<60 -> 35>=y>25
        # -x/6 + 35 for 60<=x<90 -> 25>=y>20
        f = PiecewiseLinear(n=3, worst=90, best=0)
        self.assertListEqual([-90, -60, -30, 0], f.points)
        points = [  # (-10, 0),
            (10, -10 / 2 + 50), (20, -20 / 2 + 50),
            (33, -33 / 3 + 45), (51, -51 / 3 + 45),
            (66, -66 / 6 + 35), (78, -78 / 6 + 35),
            # (100, 30)
        ]
        goal = cp.Minimize(sum([cp.abs(f.expr(x) - y) for x, y in points]))
        prob = cp.Problem(goal, f.constraints())
        error = prob.solve()
        self.assertAlmostEqual(0, error)
        for x, y in points:
            self.assertAlmostEqual(y, f.expr(x).value)


if __name__ == '__main__':
    unittest.main()
