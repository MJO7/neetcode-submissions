class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # even length palindrome
            start,end = i,i+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                res+=1
                end+=1
                start-=1
            # odd length palindrome
            start,end = i,i
            while start>=0 and end<len(s) and s[start]==s[end]:
                res+=1
                end+=1
                start-=1
            

        return res