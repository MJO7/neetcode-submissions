class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        counter = 0
        for i in nums:   
            if(i==1):
                counter+=1
            else:
                counter = 0
            res = max(res,counter)
        return res