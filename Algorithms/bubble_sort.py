import unittest

def bubble_sort(arr : list, reverse : bool = False) -> list:
    if reverse == False:
        for x in range(len(arr)):
            for y in range(1, len(arr) - x):
                if arr[y - 1] > arr[y]:
                    arr[y - 1], arr[y] = arr[y], arr[y - 1]
    else:
        for x in range(len(arr)):
            for y in range(1, len(arr) - x):
                if arr[y - 1] < arr[y]:
                    arr[y - 1], arr[y] = arr[y], arr[y - 1]
    return arr

class BubbleSortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bubble_sort([5,4,3,2,1], False), [1,2,3,4,5])

    def test_2_reverse(self):
        self.assertEqual(bubble_sort([1,2,3,4,5], True), [5,4,3,2,1])

    def test_3_sorted(self):
        self.assertEqual(bubble_sort([1,3,2,4,5], False), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()