'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
'''

import unittest

def trailingZeroes(n: int) -> int:
    zero_ct = 0
    while n > 0:
        n = n//5
        zero_ct += n
    return zero_ct

class TesttrailingZeroes(unittest.TestCase):
    def test_trailingZeroes_of_zero(self):
        self.assertEqual(trailingZeroes(0), 0)

    def test_trailingZeroes_of_positive_integer(self):
        self.assertEqual(trailingZeroes(30), 7)
        self.assertEqual(trailingZeroes(5), 1)
        # self.assertEqual(trailingZeroes(20), 2432902008176640000)

    # def test_trailingZeroes_of_negative_number(self):
    #     self.assertEqual(trailingZeroes(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()