class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I will design a solution using dictionary
        dict_s = {}
        dict_t = {}
        len_s = len(s)
        len_t = len(t)
        if(len_s!=len_t):
            return False
        else:
            for i in range(len(s)):
                dict_s[s[i]] = s.count(s[i])
                dict_t[t[i]] = t.count(t[i])
        if dict_s==dict_t:
            return True
        return False