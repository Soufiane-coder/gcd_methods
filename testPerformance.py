import unittest
from gcd_naive import gcd as gcd_naive
from gcd_euclidienne1 import gcd as gcd_euclid_1
from gcd_euclidienne_adjacted import gcd as gcd_euclid_adj
from gcd_euclidienne_recursive import result as gcd_euclid_recursive
from extended_eculid_algorithm import result as extended_gcd


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Running test:', end=' ')

    def test_gcd_naive(self):
        print('naive algorithme')
        result = gcd_naive(1, 0)
        self.assertEqual(result, 1)

        result = gcd_naive(24, 16)
        self.assertEqual(result, 8)

        result = gcd_naive(933790548, 7)
        self.assertEqual(result, 1)

        # This test will take time to get the result

        # result = gcd_naive(1849639579327, 790933790547)
        # self.assertEqual(result, 3415723)

    def test_gcd_euclid_1(self):
        print('euclidienne algorithme')
        result = gcd_euclid_1(1, 0)
        self.assertEqual(result, 1)

        result = gcd_euclid_1(24, 16)
        self.assertEqual(result, 8)

        # This test will take time to get the result
        # result = gcd_euclid_1(933790548, 7)
        # self.assertEqual(result, 1)

        result = gcd_euclid_1(1849639579327, 790933790547)
        self.assertEqual(result, 3416723)

    def test_gcd_euclid_adj(self):
        print('euclidienne algorithme plus performant')
        result = gcd_euclid_adj(1, 0)
        self.assertEqual(result, 1)

        result = gcd_euclid_adj(24, 16)
        self.assertEqual(result, 8)

        # This test will take time to get the result
        result = gcd_euclid_adj(933790548, 7)
        self.assertEqual(result, 1)

        result = gcd_euclid_adj(1849639579327, 790933790547)
        self.assertEqual(result, 3416723)

    def test_gcd_euclid_recursive(self):
        print('euclidienne algorithme plus performant recursive methode')
        result = gcd_euclid_recursive(1, 0)
        self.assertEqual(result, 1)

        result = gcd_euclid_recursive(24, 16)
        self.assertEqual(result, 8)

        # This test will take time to get the result
        result = gcd_euclid_recursive(933790548, 7)
        self.assertEqual(result, 1)

        result = gcd_euclid_recursive(1849639579327, 790933790547)
        self.assertEqual(result, 3416723)

    def test_extended_gcd(self):
        print('extended euclidienne algorithme')
        result = extended_gcd(1, 0)
        self.assertEqual(result[0], 1)

        result = extended_gcd(24, 16)
        self.assertEqual(result[0], 8)

        # This test will take time to get the result
        result = extended_gcd(933790548, 7)
        self.assertEqual(result[0], 1)

        result = extended_gcd(1849639579327, 790933790547)
        self.assertEqual(result[0], 3416723)


if __name__ == '__main__':
    unittest.main()
