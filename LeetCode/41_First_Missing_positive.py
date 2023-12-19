'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.'''

import unittest

def first_missing_positive(nums: list) -> int:
    #Brute Force
    # for x in range(1, len(nums) + 1):
    #     if x not in nums:
    #         return x
    # return len(nums) + 1    

    #more easy way
    # new= set(nums)
    # for i in range(1,len(nums)+1):
    #     if i not in new:
    #         return i
    #         break
    # return len(nums)+1

    n = len(nums)

    # Step 1: Remove non-positive and extra elements
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Step 2: Find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1 
    

class Testfirst_missing_positive(unittest.TestCase):

    # def test_first_missing_positive_of_zero(self):
    #     self.assertEqual(first_missing_positive([0]), [0])

    def test_first_missing_positive_of_positive_integer(self):
        self.assertEqual(first_missing_positive([1,2,0]), 3)
        self.assertEqual(first_missing_positive([3,4,-1,1]), 2)
        self.assertEqual(first_missing_positive([7,8,9,11,12]), 1)

    # def test_first_missing_positive_of_negative_number(self):
    #     self.assertEqual(first_missing_positive(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()