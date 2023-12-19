'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.
'''

import unittest

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def next_permutation(nums: list) -> list:
    n = len(nums)
    i = len(nums)-2
    j = 0
        
    while i>=0:
        if nums[i]<nums[i+1]:
            break
        i=i-1
                
    if (i < 0):
        nums.reverse()
    
    else:
        for j in range(n-1, i, -1):
            if (nums[j] > nums[i]):
                break
    
        swapPositions(nums, i, j)
            
        strt, end = i+1, len(nums)
    
        nums[strt:end] = nums[strt:end][::-1]
    return nums
    

class Testnext_permutation(unittest.TestCase):

    def test_next_permutation_of_zero(self):
        # self.assertEqual(next_permutation([0]), [])
        self.assertEqual(next_permutation([]), [])

    def test_next_permutation_of_positive_integer(self):
        self.assertEqual(next_permutation([1,2,3]), [1,3,2])
        self.assertEqual(next_permutation([3,2,1]), [1,2,3])
        self.assertEqual(next_permutation([1,1,5]), [1,5,1])

    # def test_next_permutation_of_negative_number(self):
    #     self.assertEqual(next_permutation(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()