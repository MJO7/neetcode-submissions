class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        prefix_product=1
        for i in range(0, len(nums)):
            prefix_array.append(prefix_product)
            prefix_product*=nums[i]
        
        suffix_array = [1]*len(nums)
        suffix_product = 1
        for j in range(len(nums)-1,-1,-1):
            suffix_array[j] = suffix_product
            suffix_product*=nums[j]

        res = []
        for i in range(len(nums)):
            res.append(suffix_array[i]*prefix_array[i])
        return res