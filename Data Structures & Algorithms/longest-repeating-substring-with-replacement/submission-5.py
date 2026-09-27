class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        countMap = defaultdict(int)

        for right in range(len(s)):
            countMap[s[right]]+=1
            windowLength = right-left+1
            frequency_of_most_appearing_char = max(countMap.values())
            while windowLength - frequency_of_most_appearing_char > k:
                countMap[s[left]]-=1
                left+=1
                frequency_of_most_appearing_char = max(countMap.values())
                windowLength-=1
            res = max(res, windowLength)

        return res