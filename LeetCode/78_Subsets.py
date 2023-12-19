"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example :
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

import unittest

def subsets(nums: list) -> list:
    output = [[]]
    for x in nums:
        output += [lst + [x] for lst in output]
    return output
    

class Testsubsets(unittest.TestCase):

    def test_subsets_of_zero(self):
        self.assertEqual(subsets([0]), [[], [0]])

    def test_subsets_of_positive_integer(self):
        self.assertEqual(subsets([1, 2, 3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        # self.assertEqual(subsets(5), 1)
        # self.assertEqual(subsets(20), 2432902008176640000)

    # def test_subsets_of_negative_number(self):
    #     self.assertEqual(subsets(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()