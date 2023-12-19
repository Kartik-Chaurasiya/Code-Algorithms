'''
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

import unittest

def maximum_subarray(nums: list) -> int:
    #Kadanes Algorithm - looks sum of consecutive elements
    max_so_far = nums[0]
    max_ending_here = nums[0]
    for x in range(1, len(nums)):
        max_ending_here = max(nums[x], max_ending_here + nums[x])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    

class Testmaximum_subarray(unittest.TestCase):

    # def test_maximum_subarray_of_zero(self):
    #     self.assertEqual(maximum_subarray([0]), [0])

    def test_maximum_subarray_of_positive_integer(self):
        self.assertEqual(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maximum_subarray([5,4,-1,7,8]), 23)
        self.assertEqual(maximum_subarray([1]), 1)

    # def test_maximum_subarray_of_negative_number(self):
    #     self.assertEqual(maximum_subarray(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()