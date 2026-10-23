class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        oneBack = 2
        twoBack = 1
        for i in range(3,n+1):
            twoBack,oneBack = oneBack, oneBack+twoBack
        return oneBack
