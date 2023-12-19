"""
Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
Example:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
"""

import unittest

def reverse_pairs(nums: list) -> int:
    # out = 0
    # # Brute Force
    # for index_x, x in enumerate(nums):
    #     for index_y, y in enumerate(nums):
    #         if index_x >= index_y:
    #             continue
    #         if x > 2 * y:
    #             out += 1
    # return out
    def merge_sort(start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = merge_sort(start, mid) + merge_sort(mid + 1, end)

        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - mid - 1)

        nums[start:end + 1] = sorted(nums[start:end + 1])
        return count

    return merge_sort(0, len(nums) - 1)
    

class Testreverse_pairs(unittest.TestCase):

    # def test_reverse_pairs_of_zero(self):
    #     self.assertEqual(reverse_pairs([0]), [0])

    def test_reverse_pairs_of_positive_integer(self):
        self.assertEqual(reverse_pairs([1,3,2,3,1]), 2)
        self.assertEqual(reverse_pairs([2,4,3,5,1]), 3)
        # self.assertEqual(reverse_pairs([7,6,4,3,1]), 0)

    # def test_reverse_pairs_of_negative_number(self):
    #     self.assertEqual(reverse_pairs(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()