class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we have to find greatest difference between a latter number in the array and earlier number
        max = 0
        for i in range(len(prices)-1,0,-1):
            for j in range(i-1, -1,-1):
                diff = prices[i]-prices[j]
                if diff>max:
                    max = diff
        return max