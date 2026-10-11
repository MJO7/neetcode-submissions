class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = 1
        prefix_array = []
        for i in range(0,len(nums)):
            prefix_array.append(prefix_product) 
            prefix_product = prefix_product*nums[i]
        
        postfix_product = 1
        postfix_array = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            postfix_array[i] = (postfix_product)
            postfix_product = postfix_product*nums[i]

        res = [1]*len(nums)
        for i in range(len(res)):
            res[i] = prefix_array[i] * postfix_array[i]
        return res