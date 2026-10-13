class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        dp = []
        oneBack = 2
        twoBack = 1
        dp = [twoBack, oneBack]
        for i in range(3,n+1):
            # new = dp[0] + dp[1]
            # dp[0] = dp[1]
            # dp[1] = new
            dp[0],dp[1] = dp[1],dp[1]+dp[0]
        return dp[1]