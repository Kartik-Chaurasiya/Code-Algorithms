import unittest

def selection_sort(arr : list, reverse : bool = False) -> list:
    if reverse == False:
        for x in range(0, len(arr) - 2):
            min_num = x
            for y in range(x+1, len(arr)):
                if arr[y] < arr[min_num]:
                    min_num = y
            if min_num != x:
                arr[min_num], arr[x] = arr[x], arr[min_num]
    else:
        for x in range(0, len(arr) - 2):
            max_num = x
            for y in range(x+1, len(arr)):
                if arr[y] > arr[max_num]:
                    max_num = y
            if max_num != x:
                arr[max_num], arr[x] = arr[x], arr[max_num]
    return arr

class SelectionSortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(selection_sort([5,4,3,2,1], False), [1,2,3,4,5])

    def test_2_reverse(self):
        self.assertEqual(selection_sort([1,2,3,4,5], True), [5,4,3,2,1])

    def test_3_sorted(self):
        self.assertEqual(selection_sort([1,3,2,4,5], False), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()