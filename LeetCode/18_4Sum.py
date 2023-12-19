"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

import unittest

def our_sum(nums: list, target: int) -> list:
    #brute force
    if len(nums) < 4:
        return []
    out = []
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            for z in range(y+1, len(nums)):
                tar_val = target - nums[x] - nums[y] - nums[z]
                if tar_val in nums[z+1:]:
                    out_temp = [tar_val, nums[x], nums[y], nums[z]]
                    if sorted(out_temp) not in out:
                        out.append(sorted(out_temp))
    return out

#can also use pointer approcah same as 3sum
    

class Testour_sum(unittest.TestCase):

    # def test_our_sum_of_zero(self):
    #     self.assertEqual(our_sum([0]), [])
    #     self.assertEqual(our_sum([]), [])

    def test_our_sum_of_positive_integer(self):
        self.assertEqual(our_sum([1,0,-1,0,-2,2], 0), [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]])
        self.assertEqual(our_sum([2,2,2,2,2], 8), [[2,2,2,2]])
        self.assertEqual(our_sum([0,0,0], 0), [])

    # def test_our_sum_of_negative_number(self):
    #     self.assertEqual(our_sum(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()