class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixFrequency=defaultdict(int)
        prefixFrequency[0] = 1
        for i in range(len(nums)):
            curSum+=nums[i]
            if (curSum-k) in prefixFrequency:
                res+=prefixFrequency[curSum-k]
            prefixFrequency[curSum]+=1
        return res