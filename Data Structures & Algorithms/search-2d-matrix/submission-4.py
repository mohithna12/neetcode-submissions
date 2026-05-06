class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] < target:
                t = m + 1
            elif matrix[m][0] > target:
                b = m - 1
            else:
                return True  # early return is fine

        row = t - 1
        if row < 0:
            return False

        while l <= r:
            c = (l + r) // 2
            if matrix[row][c] < target:
                l = c + 1
            elif matrix[row][c] > target:
                r = c - 1
            else:
                return True

        return False