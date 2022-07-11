import unittest

from OWLReadyClassMembershipFeatureSet import OWLReadyClassMembershipFeatureSet
from WikiFCDFeatureSet import WikiFCDFeatureSet
from helpers import foodon
from uta import RelativeFeatureSet, RelativeUTA


class GlutenFree(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.onto = foodon()

        cls.obo = obo = cls.onto.get_namespace("http://purl.obolibrary.org/obo/")

        # From https://en.wikipedia.org/w/index.php?title=Gluten&oldid=1093810749
        # any species of wheat (such as common wheat, durum, spelt, khorasan, emmer and einkorn), barley, rye and some oat cultivars, as well as any cross hybrids of these grains (such as triticale)
        negative_classes = [
            obo.FOODON_00001141 |  # wheat food product
            obo.FOODON_00001191 |  # barley food product
            obo.FOODON_00001189 |  # oat food product
            obo.FOODON_00001190 |  # rye food product
            obo.FOODON_00002552  # triticale food product
        ]
        positive_classes = [
            obo.FOODON_00001931  # gravy or sauce
        ]

        uta = RelativeUTA([OWLReadyClassMembershipFeatureSet([], negative_classes),
                           RelativeFeatureSet(OWLReadyClassMembershipFeatureSet(positive_classes, [])),
                           RelativeFeatureSet(WikiFCDFeatureSet())
                           ])
        # https://www.cooksmarts.com/articles/gluten-free-diet-substitutions-list/
        rankings = [
            [
                [
                    obo.FOODON_03309979,  # buckwheat noodle
                    obo.FOODON_03311767  # shirataki noodle
                ],
                [
                    obo.FOODON_03306347  # pasta
                ],
                # the following are IMO useless replacements, like replacing with raw fruits
                [
                    obo.FOODON_03301710  # apple (whole, raw)
                ]
            ],
            [
                [
                    obo.FOODON_00003751,  # sorghum seed (whole)
                    obo.FOODON_03304560  # rice (polished)
                ],
                [
                    obo.FOODON_03306062,  # barley (pearled)
                ],
                # the following are IMO useless replacements, like replacing with herbs
                [
                    obo.FOODON_03301710  # apple (whole, raw)
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
                          obo.FOODON_03302051,  # lard
                          obo.FOODON_03307541,  # white rice flour
                          obo.FOODON_03302340,  # whole wheat flour
                          obo.FOODON_03309556,  # tamari sauce
                          ]

    def test_wheat_flour_allpurpose(self):
        self.assertEqual(self.obo.FOODON_03307541, self.uta.recommend(self.obo.FOODON_03304534, self.candidates)[0])

    def test_soy_sauce(self):
        """Tamari is a gluten-free variant of soy sauce. Unfortunately FoodOn does not contain such knowledge, nor does it know that soy sauce (unless otherwise stated) is not gluten-free"""
        self.assertEqual(self.obo.FOODON_03309556, self.uta.recommend(self.obo.FOODON_03301115, self.candidates)[0])

    def test_tamari_sauce(self):
        """Tamari is a correct replacement for tamari, as it is gluten free by definition"""
        self.assertEqual(self.obo.FOODON_03309556, self.uta.recommend(self.obo.FOODON_03309556, self.candidates)[0])
