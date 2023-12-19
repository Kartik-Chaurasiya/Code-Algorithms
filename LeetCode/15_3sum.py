'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

import unittest

def three_sum(nums: list) -> list:
    nums.sort()
    out = []
    if len(nums) < 3 or nums[0] > 0:
        return []
    for x in range(len(nums) - 1):
        # 2 pointer aproach
        left = x + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[x] + nums[left] + nums[right]
            if sums < 0:
                left += 1
            elif sums > 0:
                right -= 1
            else:
                out_temp = [nums[x], nums[left], nums[right]]
                if out_temp not in out:
                    out.append(out_temp)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return out
    

class Testthree_sum(unittest.TestCase):

    def test_three_sum_of_zero(self):
        self.assertEqual(three_sum([0]), [])
        self.assertEqual(three_sum([]), [])

    def test_three_sum_of_positive_integer(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(three_sum([0,1,1]), [])
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])

    # def test_three_sum_of_negative_number(self):
    #     self.assertEqual(three_sum(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()