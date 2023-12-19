"""347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

import unittest

def TopK_Frequent_Elements(nums: list, k: int) -> list:
    top_dict = {}
    for x in nums:
        if top_dict.get(x):
            top_dict[x] += 1
        else:
            top_dict[x] = 1
    top_dict = {s: v for s, v in sorted(top_dict.items(), key=lambda item: item[1])}
    return list(top_dict.keys())[-k:]
    

class TestTopK_Frequent_Elements(unittest.TestCase):

    # def test_TopK_Frequent_Elements_of_zero(self):
    #     self.assertEqual(TopK_Frequent_Elements([0]), [0])

    def test_TopK_Frequent_Elements_of_positive_integer(self):
        self.assertEqual(TopK_Frequent_Elements([1,1,1,2,2,3], 2), [2, 1])
        self.assertEqual(TopK_Frequent_Elements([1], 1), [1])
        # self.assertEqual(TopK_Frequent_Elements(20), 2432902008176640000)

    # def test_TopK_Frequent_Elements_of_negative_number(self):
    #     self.assertEqual(TopK_Frequent_Elements(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()