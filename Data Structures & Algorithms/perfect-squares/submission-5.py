class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0]=0
        for target in range(1,n+1):
            min_squares_needed = target
            for i in range(1,n):
                if i*i<=target:
                    min_squares_needed = min(min_squares_needed,1+ dp[target-(i*i)])
                else:
                    break
            dp[target] = min_squares_needed
        return min_squares_needed