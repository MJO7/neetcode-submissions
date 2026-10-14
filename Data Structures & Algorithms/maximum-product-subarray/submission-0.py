class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMin = 1
        currentMax = 1

        for n in nums:
            if n==0: 
                currentMin = 1
                currentMax = 1
                continue
            tmp = n*currentMax
            currentMax = max(n*currentMax,n*currentMin,n)
            currentMin = min(tmp,n*currentMin,n)
            res =max(res,currentMax)

        return res