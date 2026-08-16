class Solution:
    def climbStairs(self, n: int) -> int:
        
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
            

