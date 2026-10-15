class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # botton - up
        dp = [1]*(len(nums))
        best = dp[-1]
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)