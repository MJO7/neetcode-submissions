class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        numberMap = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i = 0
        while i in range(len(s)):
            if s[i] in numberMap:
                if (i+1) < len(s) and numberMap[s[i+1]]>numberMap[s[i]]:
                    res-=numberMap[s[i]]
                else:
                    res+=numberMap[s[i]]
            i = i+1
        return res