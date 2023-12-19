import unittest

def merge_sort(arr : list, reverse : bool = False) -> list:
    if reverse == False:
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L, reverse)
            merge_sort(R, reverse)
            i = j = k = 0
            while (i < len(L)) and (j < len(R)):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            #check empty L or R
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    else:
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L, reverse)
            merge_sort(R, reverse)
            i = j = k = 0
            while (i < len(L)) and (j < len(R)):
                if L[i] >= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            #check empty L or R
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    return arr

class MergeSortTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge_sort([5,4,3,2,1], False), [1,2,3,4,5])

    def test_2_reverse(self):
        self.assertEqual(merge_sort([1,2,3,4,5], True), [5,4,3,2,1])

    def test_3_sorted(self):
        self.assertEqual(merge_sort([1,3,2,4,5], False), [1,2,3,4,5])

if __name__ == "__main__":
    unittest.main()