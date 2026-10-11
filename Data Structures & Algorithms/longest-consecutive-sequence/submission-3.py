class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        sequenceStarters = set()
        for num in nums:
            if num-1 not in nums:
                sequenceStarters.add(num)
        numberMap = {}
        for i in sequenceStarters:
            numberMap[i] = []
        for number in numberMap:
            i = number
            while i+1 in nums:
                numberMap[number].append(i+1)
                i = i+1
        
        x = numberMap.values()
        x = list(x)
        maxLen = 0
        for i in x:
            if len(i) > maxLen:
                maxLen = len(i)
        return maxLen+1