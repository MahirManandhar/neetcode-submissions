class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        mid1 = mid2 = 0
        while top<=bottom:
            mid1 = (top+bottom)//2
            if matrix[mid1][0] == target:
                return True
            elif matrix[mid1][0] > target:
                bottom = mid1 - 1
            else:
                top = mid1 + 1
        mid1 = bottom
        if mid1 < 0:
            return False    
        while left <= right:
            mid2 = (left+right)//2
            if matrix[mid1][mid2] == target:
                return True
            elif matrix[mid1][mid2] > target:
                right = mid2 - 1
            else:
                left = mid2 + 1
        return False