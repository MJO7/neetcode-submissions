class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {0:-1}
        total =0
        for i in range(len(nums)):
                total +=nums[i]
                rem = total%k
                if rem not in remainderMap:
                    remainderMap[rem] = i
                elif (i - remainderMap[rem]) > 1:
                    return True
        return False