import unittest

def partition(arr, low, high, reverse):
    if reverse == False:
        pivot = arr[high]

        i = low - 1

        for x in range(low, high):
            if arr[x] < pivot:
                i = i + 1

                arr[x], arr[i] = arr[i], arr[x]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
    else:
        pivot = arr[high]

        i = low - 1

        for x in range(low, high):
            if arr[x] > pivot:
                i = i + 1

                arr[x], arr[i] = arr[i], arr[x]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quicksort(arr, low, high, reverse):
    if low < high:
        pi = partition(arr, low, high, reverse)

        quicksort(arr, low, pi-1, reverse)

        quicksort(arr, pi + 1, high, reverse)
    return arr

def quick_sort(arr : list, reverse : bool = False) -> list:
    return quicksort(arr, 0, len(arr) - 1, reverse)
    

class QuickSortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quick_sort([5,4,3,2,1], False), [1,2,3,4,5])

    def test_2_reverse(self):
        self.assertEqual(quick_sort([1,2,3,4,5], True), [5,4,3,2,1])

    def test_3_sorted(self):
        self.assertEqual(quick_sort([1,3,2,4,5], False), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()