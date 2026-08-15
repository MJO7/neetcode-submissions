class Solution:
    def climbStairs(self, n: int) -> int:
        #Solved TOP DOWN 
        #Space Complexity is O(N)

        # memo  = {1:1, 2:2}
        
        # def dp(i):
        #     if i not in memo:
        #         memo[i] = dp(i-1)+dp(i-2)
        #     return memo[i]

        # if n>=1:
        #     return dp(n)
        # else:
        #     return 1

        #Solved BOTTOM UP
        #Space Complexity is O(1)
        if n<=2:
            return n
        
        one_back = 2      #bigger number goes in one_back
        two_back = 1

        for i in range(3,n+1):
            current = one_back + two_back
            two_back = one_back
            one_back = current

        return  one_back
            

