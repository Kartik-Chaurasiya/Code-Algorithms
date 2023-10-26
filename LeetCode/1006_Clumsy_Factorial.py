'''
1006. Clumsy Factorial

We make a clumsy factorial using the integers in decreasing order by swapping out the multiply 
operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' 
in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
'''

import unittest

def clumsy(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 7
    if n % 4 == 1:
        return n + 2
    if n % 4 == 2:
        return n + 2
    if n % 4 == 3:
        return n - 1
    return n + 1

class Testclumsy(unittest.TestCase):
    # def test_clumsy_of_zero(self):
    #     self.assertEqual(clumsy(0), 1)

    def test_clumsy_of_positive_integer(self):
        self.assertEqual(clumsy(4), 7)
        self.assertEqual(clumsy(10), 12)
        # self.assertEqual(clumsy(20), 2432902008176640000)

    # def test_clumsy_of_negative_number(self):
    #     self.assertEqual(clumsy(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()