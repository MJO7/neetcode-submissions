class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. make a set to store the unique characters
        # 2. left pointer at 0,
        # 3. right pointer in the for loop
        
        charSet = set()
        left = 0
        max_substring_length = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            max_substring_length = max(max_substring_length, (right-left+1))

        return max_substring_length
        