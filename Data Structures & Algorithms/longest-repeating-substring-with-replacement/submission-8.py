class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        countMap = defaultdict(int)
        maxFrequency = 0
        for right in range(len(s)):
            countMap[s[right]]+=1
            maxFrequency = max(maxFrequency, countMap[s[right]])
            windowLength = right-left+1
            while windowLength - maxFrequency > k:
                countMap[s[left]]-=1
                left+=1
                windowLength-=1
            res = max(res, windowLength)

        return res