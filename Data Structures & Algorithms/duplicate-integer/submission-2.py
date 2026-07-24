class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i+1,l):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        
        # with O(N) complexity

        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            numsSet.add(i)
        return False
        

