class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # OPTIMAL SOLUTION
        res,count = 0,0
        for n in nums:
            if count==0:
                count+=1
                res = n
            if res==n:
                count+=1
            else:
                count-=1
        return res