class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_res = 0
        while left<right:
            max_res = max(max_res, min(heights[left],heights[right])*(right-left))
            if heights[left]<=heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
        return max_res