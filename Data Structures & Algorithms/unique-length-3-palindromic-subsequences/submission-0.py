class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for char in set(s):
            first_occurence_index = s.index(char)
            last_occurence_index = s.rindex(char)
            if first_occurence_index!=last_occurence_index:
                res+=len(set(s[first_occurence_index+1:last_occurence_index]))
        return res
