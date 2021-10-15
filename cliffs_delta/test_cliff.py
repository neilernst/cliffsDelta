import unittest

from __init__ import cliffs_delta

class MyTest(unittest.TestCase):

    def test_small_difference(self):
        """ test data from Marco Torchiano R package https://github.com/mtorchiano/effsize"""
        treatment = [10, 10, 20, 20, 20, 30, 30, 30, 40, 50]
        control = [10, 20, 30, 40, 40, 50]

        d, res = cliffs_delta(treatment, control)
        # Cliff's Delta
        #
        # delta estimate: -0.25 (small)
        # 95 percent confidence interval:
        #  inf        sup
        # -0.7265846  0.3890062
        self.assertEqual("small", res)
        self.assertEqual(d, -0.25)

    def test_tim(self):
        lst1 = range(8)
        out = []
        expected = ['negligible','negligible','small','small', 'medium']
        for r in [1.01, 1.1, 1.21, 1.5, 2]:
            lst2 = list(map(lambda x: x * r, lst1))
            d, res = cliffs_delta(lst1, lst2)
            out.append(res)

        self.assertEqual(expected,out)

    def test_negligible(self): #Marco
        x1 = [10, 20, 20, 20, 30, 30, 30, 40, 50, 100]
        x2 = [10, 20, 30, 40, 40, 50]
        d, res = cliffs_delta(x1, x2)
        self.assertAlmostEqual(-0.06667, d, 4)

    def test_nonoverlapping(self): # marco's test
        x1 = [10, 20, 20, 20, 30, 30, 30, 40, 50, 100]
        x2 = [10, 20, 30, 40, 40, 50]
        factor = 110
        x2 = [x+factor for x in x2]

        d, res = cliffs_delta(x1, x2)
        self.assertEqual(res, 'large')
        self.assertAlmostEqual(d, -1, 2)

if __name__ == '__main__':
    unittest.main()