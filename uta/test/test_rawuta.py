import unittest

from uta import RawUTA


class RawUTATest(unittest.TestCase):
    # http://www.cs.put.poznan.pl/imaslowska/wd/lab9/Metoda%20UTA.pdf

    def test1(self):
        variants = {"Ford Mondeo": (26000, 145),
                    "Peugot 308": (20000, 120),
                    "Fiat Panda": (8000, 70),
                    "Skoda Fabia": (14000, 95),
                    "VW Passat": (32000, 170)}

        reference_ranking = [
            ["Skoda Fabia"],
            ["Fiat Panda"],
            ["VW Passat"]
        ]
        uta = RawUTA([(2, 32000, 8000), (2, 70, 170)])
        uta.add(reference_ranking, variants)
        d = uta.solve()
        self.assertAlmostEqual(d, 0.0)
        self.assertAlmostEqual(uta.U([32000, 70]).value, 0.0)
        self.assertAlmostEqual(uta.U([8000, 170]).value, 1.0)
        self.assertGreater(uta.U(variants["Skoda Fabia"]).value, uta.U(variants["Fiat Panda"]).value)
        self.assertGreater(uta.U(variants["Fiat Panda"]).value, uta.U(variants["VW Passat"]).value)
        self.assertGreater(uta.U([17000, 121]).value, uta.U(variants["VW Passat"]).value)

    def test2(self):
        variants = {"jajka gotowane": (6.58, 155, 12.5, 50, 50, 0),
                    "brokuł": (8, 27, 3, 48, 20, 2.5),
                    "płatki owsiane": (8, 379, 11.9, 54, 57, 6.9),
                    "marchewka": (2.5, 40, 1.1, 41, 63, 4),
                    "ryż brązowy": (7.6, 357, 7.1, 32, 65, 8.7),
                    "makaron razowy": (22, 357, 15.2, 49, 37, 8.3)}
        reference_ranking = [
            ["makaron razowy"],
            ["ryż brązowy", "marchewka"],
            ["brokuł"]
        ]
        uta = RawUTA([
            (2, 22, 2),
            (2, 20, 392),
            (2, 0.4, 15.2),
            (2, 2.22, 610),
            (2, 90, 10),
            (2, 0, 8.7)
        ])
        uta.add(reference_ranking, variants)
        d = uta.solve()
        self.assertAlmostEqual(d, 0.0)
        mr = uta.U(variants["makaron razowy"]).value
        rb = uta.U(variants["ryż brązowy"]).value
        m = uta.U(variants["marchewka"]).value
        b = uta.U(variants["brokuł"]).value
        po = uta.U(variants["płatki owsiane"]).value
        self.assertGreater(mr, rb)
        self.assertAlmostEqual(rb, m)
        self.assertGreater(m, b)
        self.assertGreater(mr, po)
        self.assertGreater(po, rb)


if __name__ == '__main__':
    unittest.main()
