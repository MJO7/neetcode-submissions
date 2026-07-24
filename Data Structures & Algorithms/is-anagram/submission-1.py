class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I will design a solution using dictionary

        #O(N) solution
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        
        return dict_s == dict_t
        #O(N^2) solution
        # dict_s = {}
        # dict_t = {}
        # len_s = len(s)
        # len_t = len(t)
        # if(len_s!=len_t):
        #     return False
        # else:
        #     for i in range(len(s)):
        #         dict_s[s[i]] = s.count(s[i])
        #         dict_t[t[i]] = t.count(t[i])
        # if dict_s==dict_t:
        #     return True
        # return False