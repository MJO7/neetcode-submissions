class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # OPTIMIZED SOLUTION
        
        # if target is less than last integer of current row : 
        # then do binary search on that row
        # else: move to the next row

        left_ptr_for_row = 0
        right_ptr_for_row = len(matrix)-1


        while left_ptr_for_row<=right_ptr_for_row:
            mid_ptr_for_row = left_ptr_for_row+((right_ptr_for_row-left_ptr_for_row)//2)
            if target > matrix[mid_ptr_for_row][len(matrix[mid_ptr_for_row])-1]:
                left_ptr_for_row = mid_ptr_for_row+1
            elif target < matrix[mid_ptr_for_row][0]:
                right_ptr_for_row = mid_ptr_for_row-1
            else:
                break

        if not (left_ptr_for_row<=right_ptr_for_row):
            return False
        
        index_of_row_with_target = mid_ptr_for_row
        left = 0
        right = len(matrix[index_of_row_with_target])-1

        while left<=right:
            mid = left+((right-left)//2)
            if target>matrix[index_of_row_with_target][mid]:
                left = mid+1
            elif target<matrix[index_of_row_with_target][mid]:
                right = mid-1
            else:
                return True

        return False