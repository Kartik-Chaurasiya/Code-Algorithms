'''
283. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

import unittest

def move_zeros(nums: list) -> list:
    zero_pos = 0
    for x in range(len(nums)):
        if nums[x] != 0:
            nums[zero_pos], nums[x] = nums[x], nums[zero_pos]
            zero_pos += 1
    return nums
    

class Testmove_zeros(unittest.TestCase):

    def test_move_zeros_of_zero(self):
        self.assertEqual(move_zeros([0]), [0])

    def test_move_zeros_of_positive_integer(self):
        self.assertEqual(move_zeros([0,1,0,3,12]), [1,3,12,0,0])
        # self.assertEqual(move_zeros(5), 1)
        # self.assertEqual(move_zeros(20), 2432902008176640000)

    # def test_move_zeros_of_negative_number(self):
    #     self.assertEqual(move_zeros(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()