class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        for i in t:
            countT[i]+=1

        have = 0
        need = len(countT)

        res = [-1,-1]
        resLen = float("infinity")

        left = 0
        for right in range(len(s)):
            window[s[right]]+=1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have+=1
            while have==need:
                if (right-left+1)<resLen:
                    res = [left,right]
                    resLen = right-left+1
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                left+=1

        if resLen!=float("infinity"):
            l,r = res
            return s[l:r+1]
        else:
            return ""


        