class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse() # flips the matrix upside down

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # TC: O(n^2) SC: O(1)