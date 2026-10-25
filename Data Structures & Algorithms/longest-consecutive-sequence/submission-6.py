class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sequenceStarterMap = {}
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                sequenceStarterMap[i] = []
        for i in sequenceStarterMap:
            next_element = i+1
            while next_element in nums:
                sequenceStarterMap[i].append(next_element)
                next_element+=1
        maxLen = 0
        sequenceList = list(sequenceStarterMap.values())
        for i in sequenceList:
            if len(i)>maxLen:
                maxLen = len(i)
        return maxLen+1