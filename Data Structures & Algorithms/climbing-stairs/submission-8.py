class Solution:
    def climbStairs(self, n: int) -> int:
        #Solved TOP DOWN 
        #Space Complexity is O(N)

        memo  = {1:1, 2:2}
        
        def dp(i):
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)
            return memo[i]

        if n>=1:
            return dp(n)
        else:
            return 1
