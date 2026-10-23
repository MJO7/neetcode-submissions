class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp["last"] = 0
        dp["secondLast"] = cost[-1]
        for i in range(len(cost)-2,-1,-1):
            temp = cost[i] + min(dp["secondLast"],dp["last"])
            dp["last"] = dp["secondLast"]
            dp["secondLast"] = temp
        return min(dp["last"],dp["secondLast"])
            