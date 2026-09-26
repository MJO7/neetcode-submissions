class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix & suffix arrays
        n = len(height)
        if n==0:
            return 0

       
        leftMax = [0]*n
        rightMax = [0]*n
        
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])

        for j in range(n-2,-1,-1):
            rightMax[j
            ] = max(rightMax[j+1], height[j])

        res = 0

        for index in range(0,n):
            res+=min(leftMax[index],rightMax[index]) - height[index]

        return res



        