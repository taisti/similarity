import unittest

from OWLReadyClassMembershipFeatureSet import OWLReadyClassMembershipFeatureSet
from WikiFCDFeatureSet import WikiFCDFeatureSet
from helpers import foodon
from uta import RelativeFeatureSet, RelativeUTA


class Vegan(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.onto = foodon()

        cls.obo = obo = cls.onto.get_namespace("http://purl.obolibrary.org/obo/")

        negative_classes = [
            obo.FOODON_00001092 |  # vertebrate animal food product
            obo.FOODON_00001046 |  # seafood product
            obo.FOODON_00001176,  # invertebrate food product
            obo.FOODON_00001242  # spice or herb
        ]
        positive_classes = [
            obo.FOODON_00001184 |  # algal food product
            obo.FOODON_00001143 |  # 'fungus food product'
            obo.FOODON_00001145 |  # 'microbial food product'
            obo.FOODON_00001015 |  # 'plant food product'
            obo.FOODON_00002131 |  # 'plant based refined or partially-refined food product'
            obo.FOODON_00002129  # 'plant based meat product analog'
        ]

        uta = RelativeUTA([OWLReadyClassMembershipFeatureSet(positive_classes, negative_classes),
                           RelativeFeatureSet(WikiFCDFeatureSet())
                           ])

        rankings = [
            # http://www.foodsubs.com/MeatcureBacon.html
            [
                [
                    obo.FOODON_03305199,  # imitation bacon bit
                ],
                [
                    obo.FOODON_03309992  # bacon (smoked)
                ],
                # the following are IMO useless replacements, like replacing with raw fruits
                [
                    obo.FOODON_03301710  # [apple (whole, raw)]()
                ]
            ],
            # http://www.foodsubs.com/Meats.html
            [
                [
                    obo.FOODON_03304999,  # 'tempeh'
                    obo.FOODON_03309664,  # 'tofu food product'
                    obo.FOODON_03311469  # 'vegetable protein (textured)'
                ],
                [
                    obo.FOODON_03309737,  # 'beef (raw)'
                    obo.FOODON_03311109,  # 'turkey (raw, ground)'
                ],
                # the following are IMO useless replacements, like replacing with herbs
                [
                    obo.FOODON_03301215,  # 'thyme (dried)'
                    obo.FOODON_00003738,  # 'vanilla bean (whole)'
                ]
            ]]
        for ranking in rankings:
            assert len(ranking) == 3
            for reference in ranking[1]:
                uta.add(reference, ranking[0], ranking[2])
        uta.solve()
        cls.uta = uta

        cls.candidates = [obo.FOODON_03303520,  # 'red kidney bean (canned)'
                          obo.FOODON_03301710,  # apple
                          obo.FOODON_03302578,  # canola oil
                          obo.FOODON_03310809,  # wheat gluten
                          obo.FOODON_03302051  # lard
                          ]

    def test_pork_fresh(self):
        self.assertEquals(self.obo.FOODON_03303520, self.uta.recommend(self.obo.FOODON_03317271, self.candidates)[0])

    def test_beef_raw(self):
        self.assertEquals(self.obo.FOODON_03303520, self.uta.recommend(self.obo.FOODON_03309737, self.candidates)[0])

    def test_tallow(self):
        self.assertEquals(self.obo.FOODON_03302578, self.uta.recommend(self.obo.FOODON_03315521, self.candidates)[0])

    def test_honey(self):
        self.assertEquals(self.obo.FOODON_03301710, self.uta.recommend(self.obo.UBERON_0036016, self.candidates)[0])
