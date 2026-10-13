class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0,0

        for money in nums:
            best = max(rob1+money,rob2)
            rob1 = rob2
            rob2 = best
        return rob2