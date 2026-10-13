class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        i = 1
        while i<len(intervals):
            # first check IF they're overlapping
            if intervals[i-1][1]>intervals[i][0]:
                res+=1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
            i = i+1
        
        return res