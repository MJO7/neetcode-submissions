class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        one = 1
        two = 2
        for i in range(3,n+1):
            one,two = two, one+two
        return two