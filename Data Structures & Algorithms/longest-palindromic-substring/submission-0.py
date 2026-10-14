class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        n = len(s)
        res = ""

        for i in range(n):
            # if palindrome is odd length
            start,end = i,i
            while start>=0 and end<n and s[start]==s[end]:
                newLength = (end-start)+1
                if newLength>resLen:
                    resLen = max(resLen, newLength)
                    res = s[start:end+1]
                start -=1
                end+=1
            # if palindrome is even
            start,end = i,i+1
            while start>=0 and end<n and s[start]==s[end]:
                newLength = (end-start)+1
                if newLength>resLen:
                    resLen = max(resLen, newLength)
                    res = s[start:end+1]
                start -=1
                end+=1
        
        return res