import unittest
from delivery_calc import *


class MyTestCase(unittest.TestCase):
    def test_0(self):
        res = truck_loads(0)
        self.assertEqual(res, [0])

    def test_1(self):
        res = truck_loads(1)
        self.assertEqual(res, [1])

    def test_40(self):
        res = truck_loads(40)
        self.assertEqual(res, [40])

    def test_41(self):
        res = truck_loads(41)
        self.assertEqual(res, [21, 20])

    def test_100(self):
        res = truck_loads(100)
        self.assertEqual(res, [34, 33, 33])

    def test_205(self):
        res = truck_loads(205)
        self.assertEqual(res, [35, 34, 34, 34, 34, 34])

    def test_208(self):
        res = truck_loads(208)
        self.assertEqual(res, [35, 35, 35, 35, 34, 34])

    def test_500(self):
        res = truck_loads(500)
        self.assertEqual(res, [39, 39, 39, 39, 39, 39, 38, 38, 38, 38, 38, 38, 38])

    def test_1000(self):
        res = truck_loads(1000)
        self.assertEqual(res, [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
                               40, 40, 40])

    def test_negative(self):
        res = truck_loads(0)
        self.assertEqual(res, [0])

    def test_char(self):
        res = truck_loads('abc')
        self.assertEqual(res, None)






if __name__ == '__main__':
    unittest.main()
