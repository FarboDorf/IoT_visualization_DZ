import unittest
from tax_calc import *


class MyTestCase(unittest.TestCase):
    def test_0(self):
        res = tax(0)
        self.assertEqual(res, 0)

    def test_50000(self):
        res = tax(50000)
        self.assertEqual(res, 0)

    def test_150000(self):
        res = tax(150000)
        self.assertEqual(res, 2500)

    def test_250000(self):
        res = tax(250000)
        self.assertEqual(res, 7500)

    def test_250001(self):
        res = tax(250001)
        self.assertEqual(res, 7500.1)

    def test_1000000(self):
        res = tax(1000000)
        self.assertEqual(res, 82500)

    def test_1000001(self):
        res = tax(1000001)
        self.assertEqual(res, 82500.2)

    def test_minus1(self):
        res = tax(-1)
        self.assertEqual(res, 0)

    def test_char(self):
        res = tax('abc')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
