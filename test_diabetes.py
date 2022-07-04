import unittest

from WikiFCDFeatureSet import WikiFCDFeatureSet
from helpers import foodon
from uta import RelativeFeatureSet, RelativeUTA


class Diabetes(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.onto = foodon()

        cls.obo = obo = cls.onto.get_namespace("http://purl.obolibrary.org/obo/")

        uta = RelativeUTA([
            WikiFCDFeatureSet(),
            RelativeFeatureSet(WikiFCDFeatureSet())
        ])

        rankings = [
            [
                # https://www.gifoundation.com/food-list/flour/
                [
                    obo.FOODON_03302142  # soybean flour
                ],
                [
                    obo.FOODON_03302492  # rye flour
                ],
                [
                    obo.FOODON_03307541  # white rice flour
                ]
            ]
        ]
        for ranking in rankings:
            assert len(ranking) == 3
            for reference in ranking[1]:
                uta.add(reference, ranking[0], ranking[2])
        uta.solve()
        cls.uta = uta

        cls.candidates_no_chickpea = [
            obo.FOODON_03310681,  # tapioca flour
            obo.FOODON_00003351,  # brown rice flour
            obo.FOODON_03307543  # potato starch
        ]

        cls.candidates = cls.candidates_no_chickpea + [
            obo.FOODON_03304537,  # chickpea flour
        ]

    def test_tapioca_flour(self):
        self.assertEquals(self.obo.FOODON_03304537, self.uta.recommend(self.obo.FOODON_03310681, self.candidates)[0])

    def test_brown_rice_flour(self):
        self.assertEquals(self.obo.FOODON_03304537, self.uta.recommend(self.obo.FOODON_00003351, self.candidates)[0])

    def test_chickpea_flour(self):
        self.assertEquals(self.obo.FOODON_03304537, self.uta.recommend(self.obo.FOODON_03304537, self.candidates)[0])

    def test_potato_starch(self):
        self.assertEquals(self.obo.FOODON_03304537, self.uta.recommend(self.obo.FOODON_03307543, self.candidates)[0])

    def test_tapioca_flour_no_chickpea(self):
        self.assertEquals(self.obo.FOODON_00003351,
                          self.uta.recommend(self.obo.FOODON_03310681, self.candidates_no_chickpea)[0])

    def test_brown_rice_flour_no_chickpea(self):
        self.assertEquals(self.obo.FOODON_00003351,
                          self.uta.recommend(self.obo.FOODON_00003351, self.candidates_no_chickpea)[0])

    def test_potato_starch_no_chickpea(self):
        self.assertEquals(self.obo.FOODON_00003351,
                          self.uta.recommend(self.obo.FOODON_03307543, self.candidates_no_chickpea)[0])
