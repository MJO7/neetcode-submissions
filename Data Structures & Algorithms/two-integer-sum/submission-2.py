class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i,n in enumerate(nums): 
            mydict[n]=i

        for i,n in enumerate(nums):
            diff = target-n
            if diff in mydict and mydict[diff]!=i:
                return [i,mydict[diff]]

        return [] 