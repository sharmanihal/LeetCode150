### Solution 1:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # With m*n Space complexity
        copy = [list(row) for row in matrix]
        for arrayIndex, array in enumerate(copy):
            for elementIndex, element in enumerate(array):
                if element == 0:
                    for i in range(0, len(matrix)):
                        matrix[i][elementIndex] = 0
                    for i in range(0, len(matrix[0])):
                        matrix[arrayIndex][i] = 0
"""
Explanation:
- This solution first creates a copy of the original matrix.
- It then iterates over the copy, and whenever it encounters a zero element, it sets the entire corresponding column and row in the original matrix to zero.
"""


### Solution 2:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # With m+n Space Complexity
        column = [1] * len(matrix[0])
        row = [1] * len(matrix)
        for arrayIndex, array in enumerate(matrix):
            for elementIndex, element in enumerate(array):
                if element == 0:
                    row[arrayIndex] = 0
                    column[elementIndex] = 0
        for index, ele in enumerate(row):
            if ele == 0:
                for i in range(len(matrix[0])):
                    matrix[index][i] = 0
        for index, ele in enumerate(column):
            if ele == 0:
                for i in range(len(matrix)):
                    matrix[i][index] = 0
"""
Explanation:
- This solution uses additional arrays `row` and `column` to keep track of which rows and columns need to be zeroed out.
- It iterates over the matrix to mark the rows and columns containing zeros.
- Then, it updates the original matrix based on the information stored in the `row` and `column` arrays.
"""


### Solution 3:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # With constant space
        row, column = len(matrix), len(matrix[0])
        rowZero = False
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        for i in range(1, row):
            for j in range(1, column):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(row):
                matrix[i][0] = 0
        if rowZero:
            for i in range(column):
                matrix[0][i] = 0
"""
Explanation:
- This solution utilizes the first row and first column of the matrix itself to mark the rows and columns that need to be zeroed out.
- It iterates through the matrix, marking the first row and first column appropriately whenever it encounters a zero element.
- Then, it traverses the matrix again, except for the first row and first column, and sets zeros based on the markings made in the first row and first column.
- Finally, it handles the special cases where the first row or column itself contains zeros, ensuring those rows and columns are zeroed out accordingly.
"""
