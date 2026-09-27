class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target is less than last integer of current row : 
        # then do binary search on that row
        # else: move to the next row

        for row in matrix:
            last_int = row[len(row)-1]
            if target==last_int:
                return True
            elif target<last_int:
                left = 0
                right = len(row)-1
                while left<=right:
                    mid = left+((right-left)//2)
                    if target>row[mid]:
                        left = mid+1
                    elif target<row[mid]:
                        right = mid-1
                    else:
                        return True
        return False
                