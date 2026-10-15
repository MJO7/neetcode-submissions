class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def canMake(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums) or remaining < 0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = (
                canMake(i + 1, remaining) or
                canMake(i + 1, remaining - nums[i])
            )
            return memo[(i, remaining)]

        return canMake(0, target)