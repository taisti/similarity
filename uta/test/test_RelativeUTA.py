import unittest

from uta import FeatureDescriptor, DictFeatureSet, RelativeFeatureSet, RelativeUTA


class RelativeUTATest(unittest.TestCase):
    def test_onlyrelative(self):
        data = {
            'a1': (1, 1),
            'b1': (1, 2),
            'a2': (2, 5),
            'b2': (2, 7),
            'a3': (3, 9),
            'b3': (3, 12),
        }
        descriptors = [
            FeatureDescriptor('F1', 1, 0, 5),
            FeatureDescriptor('F2', 1, 0, 20)
        ]
        features = DictFeatureSet(data, descriptors)
        ruta = RelativeUTA([RelativeFeatureSet(features)])
        ruta.add('a1', ['b1'], ['b2', 'a2'])
        ruta.solve()

        def recommend(reference):
            return ruta.recommend(reference, list(data.keys() - {reference}))[0]

        self.assertEquals("b1", recommend("a1"))
        self.assertEquals("a1", recommend("b1"))
        self.assertEquals("b2", recommend("a2"))
        self.assertEquals("a2", recommend("b2"))
        self.assertEquals("b3", recommend("a3"))
        self.assertEquals("a3", recommend("b3"))

    def test_mixed(self):
        data1 = {
            'a1': (1,),
            'b1': (1,),
            'c1': (1,),
            'a2': (2,),
            'b2': (2,),
            'c2': (2,),
            'a3': (3,),
            'b3': (3,),
            'c3': (3,),
        }
        data2 = {
            'a1': (1,),
            'b1': (2,),
            'c1': (3,),
            'a2': (1,),
            'b2': (2,),
            'c2': (3,),
            'a3': (1,),
            'b3': (2,),
            'c3': (3,),
        }

        features = [
            RelativeFeatureSet(DictFeatureSet(data1, [FeatureDescriptor('F1', 1, 0, 5)])),
            DictFeatureSet(data2, [FeatureDescriptor('F2', 1, 5, 0)]),
        ]
        ruta = RelativeUTA(features)
        ruta.add('a1', ['b1'], ['b2', 'a2'])
        ruta.solve()

        for reference in data1.keys():
            print("reference", reference)
            for variant in data1.keys() - {reference}:
                print(variant, ruta.U(reference, variant))

        def recommend(reference):
            return ruta.recommend(reference, list(data1.keys() - {reference}))[0]

        self.assertEquals("b1", recommend("a1"))
        self.assertEquals("a1", recommend("b1"))
        self.assertEquals("a1", recommend("c1"))
        self.assertEquals("b2", recommend("a2"))
        self.assertEquals("a2", recommend("b2"))
        self.assertEquals("a2", recommend("c2"))
        self.assertEquals("b3", recommend("a3"))
        self.assertEquals("a3", recommend("b3"))
        self.assertEquals("a3", recommend("c3"))


if __name__ == '__main__':
    unittest.main()
