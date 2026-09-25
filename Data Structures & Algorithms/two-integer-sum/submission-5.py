class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hashmap like so:
        # key = number, value = it's index 
        prevMap = {}
        for i in range(0,len(nums)):
            if (target-nums[i]) in prevMap:
                return [prevMap[target-nums[i]],i]
            else:
                prevMap[nums[i]] = i

        return []

        # solving in one pass