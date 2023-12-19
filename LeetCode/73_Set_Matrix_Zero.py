"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example :
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

import unittest

def set_matrix_zero(matrix: list) -> list:
    row_flag = col_flag = False
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                if row == 0:
                    row_flag = True
                if col == 0:
                    col_flag = True
                else:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][0] ==0 or matrix[0][col] == 0:
                matrix[row][col] = 0
    if row_flag == True:
        matrix[0] = [0]*len(matrix[0])
    if col_flag == True:
        for row in range(len(matrix)):
            matrix[row][0] = 0
    return matrix
    

class Testset_matrix_zero(unittest.TestCase):

    # def test_set_matrix_zero_of_zero(self):
    #     self.assertEqual(set_matrix_zero([0]), [[], [0]])

    def test_set_matrix_zero_of_positive_integer(self):
        self.assertEqual(set_matrix_zero([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(set_matrix_zero([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        # self.assertEqual(set_matrix_zero(20), 2432902008176640000)

    # def test_set_matrix_zero_of_negative_number(self):
    #     self.assertEqual(set_matrix_zero(-1), 'Not Defined')

if __name__ == '__main__':
    unittest.main()