import unittest

def insertion_sort(arr : list, reverse : bool = False) -> list:
    if reverse == False:
        for x in range(1, len(arr)):
            curr = arr[x]
            y = x - 1
            while (y >= 0) & (curr < arr[y]):
                arr[y + 1] = arr[y]
                # arr[y + 1], arr[y] = arr[y], arr[y + 1]
                y = y - 1
            arr[y + 1] = curr
    else:
        for x in range(1, len(arr)):
            curr = arr[x]
            y = x - 1
            while (y >= 0) & (curr > arr[y]):
                arr[y + 1] = arr[y]
                y = y - 1
            arr[y + 1] = curr
    return arr

class InssertionSortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(insertion_sort([5,4,3,2,1], False), [1,2,3,4,5])

    def test_2_reverse(self):
        self.assertEqual(insertion_sort([1,2,3,4,5], True), [5,4,3,2,1])

    def test_3_sorted(self):
        self.assertEqual(insertion_sort([1,3,2,4,5], False), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()