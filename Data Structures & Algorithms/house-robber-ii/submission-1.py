class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1=0
        rob2= 0
        n = len(nums)
        for money in range(0,n-1):
            best = max(rob1+nums[money], rob2)
            rob1 = rob2
            rob2 = best
        max_first_portion = rob2
        rob1=0
        rob2= 0
        for money in range(1,n):
            best = max(rob1+nums[money], rob2)
            rob1 = rob2
            rob2 = best
        return max(rob2, max_first_portion)

