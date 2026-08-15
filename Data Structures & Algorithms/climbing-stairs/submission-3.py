class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==1:
        #     return 1
        # one = 1
        # two = 2
        # for i in range(3,n+1):
        #     one,two = two, one+two
        # return two

        #Solved TOP DOWN
        memo  = {1:1, 2:2}
        
        def dp(i):
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)
            return memo[i]

        if n>=1:
            return dp(n)
        else:
            return 1