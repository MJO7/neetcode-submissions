class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter_s = defaultdict(int)
        for i in s:
            counter_s[i]+=1
        counter_t = defaultdict(int)
        for j in t:
            counter_t[j]+=1
        for char in s:
            if counter_s[char]!=counter_t[char]:
                return False
        return True