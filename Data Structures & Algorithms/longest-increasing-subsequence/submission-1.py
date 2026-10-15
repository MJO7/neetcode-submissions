class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at dp[i], what exactly is the length of the longest strictly increasing subsequence
        memo = {}
        def maxLength(i):
            best = 1  # Just nums[i]
            if i in memo:
                return memo[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + maxLength(j))
            memo[i] = best
            return best

        return max(maxLength(i) for i in range(len(nums)))