'''The factorial problem involves finding the factorial of a non-negative integer. 
The factorial of a non-negative integer n is the product of all positive integers from 1 to n. 
It's often denoted as n! and is defined as:

n! = n × (n - 1) × (n - 2) × ... × 2 × 1

5! = 5 × 4 × 3 × 2 × 1 = 120

'''

import unittest

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'Not Defined'
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_of_negative_number(self):
        self.assertEqual(factorial(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()