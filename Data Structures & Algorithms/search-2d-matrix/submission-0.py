class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in range(0, len(matrix)):
            for m in range(0, len(matrix[n])):
                if target == matrix[n][m]:
                    return True
        return False