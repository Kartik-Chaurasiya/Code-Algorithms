'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

import unittest

def container_with_most_water(height: list) -> int:
    water = 0
    left = 0
    right = len(height) - 1
    while left < right:
        ht = min(height[left], height[right])
        wdt = abs(left - right)
        if water < ht * wdt:
            water = ht * wdt
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return water
    

class Testcontainer_with_most_water(unittest.TestCase):

    # def test_container_with_most_water_of_zero(self):
    #     self.assertEqual(container_with_most_water([0]), [0])

    def test_container_with_most_water_of_positive_integer(self):
        self.assertEqual(container_with_most_water([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(container_with_most_water([1,1]), 1)
        # self.assertEqual(container_with_most_water(20), 2432902008176640000)

    # def test_container_with_most_water_of_negative_number(self):
    #     self.assertEqual(container_with_most_water(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()