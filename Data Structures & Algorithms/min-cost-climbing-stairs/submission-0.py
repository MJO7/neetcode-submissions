class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp["last"] = 0
        dp["secondLast"] = cost[-1]
        n = len(cost)
        for i in range(n-2,-1,-1):
            tmp =  cost[i]+ min(dp["secondLast"],dp["last"])
            dp["last"] = dp["secondLast"]
            dp["secondLast"] = tmp
        return min(dp["last"],dp["secondLast"])