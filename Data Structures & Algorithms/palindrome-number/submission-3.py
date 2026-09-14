class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converting to string OPTIMAL solution
        # use two pointer for start and end

        #Algorithm:
        # convert to string first
        #set pointer for start i and end j
        # loop till len(x)-1/2 and compare x[i] and x[len(x)-1-i]

        s = str(x)
        n = len(s)

        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
        return True