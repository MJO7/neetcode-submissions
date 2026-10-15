class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}
        def targetSum(i,remaining):

            if remaining==0:
                return True
            if (i,remaining) in memo:
                return memo[(i,remaining)]
            if i==len(nums) or remaining<0:
                return False
            memo[(i,remaining)] = targetSum(i+1, remaining-nums[i]) or targetSum(i+1, remaining)
            return targetSum(i+1, remaining-nums[i]) or targetSum(i+1, remaining)
        
        return targetSum(0,target)