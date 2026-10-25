class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_r = 0
        right_r = len(matrix)-1
        while left_r<=right_r:
            mid = left_r+((right_r-left_r)//2)
            if target<matrix[mid][0]:
                right_r = mid-1
            elif target>matrix[mid][-1]:
                left_r = mid+1
            else:
                break
        if left_r>right_r:
            return False
        row_with_target = mid
        # now binary seach in that row
        left = 0
        right = len(matrix[row_with_target])-1
        while left<=right:
            mid = left+((right-left)//2)
            if target<matrix[row_with_target][mid]:
                right = mid-1
            elif target>matrix[row_with_target][mid]:
                left = mid + 1
            else:
                return True
        return False