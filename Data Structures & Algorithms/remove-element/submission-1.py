class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k = k+1
        return k

        #O(N^2)
        # k = 0
        # i = 0 
        # l = len(nums)
        # while ( < l):
        #     if nums[i]==val:
        #         nums.pop(i)
        #         i = i-1
        #         l = l-1
        #     else:
        #         k = k+1
            
        #     i = i+1
        # return k