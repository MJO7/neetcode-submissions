class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. for each number, in the rest of the array, we wanna find if there's two numbers that add to it's additive inverse
        # 
        nums.sort()
        list_of_3_sums = []
        for i in range(0,len(nums)):
            target = -(nums[i])
            prevMap = {}

            for index in range(i+1,len(nums)):
                
                if (target - nums[index]) in prevMap:
                    
                    to_be_appended = [nums[i], (target-nums[index]), nums[index]]
                    if to_be_appended not in list_of_3_sums:
                        list_of_3_sums.append(to_be_appended )
                else:
                    prevMap[nums[index]] = index 

        return list_of_3_sums
                