"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        res = 0
        start_index = 0
        end_index = 0
        count = 0
        while start_index<len(intervals) and end_index<len(intervals):
            if start[start_index]<end[end_index]:
                count+=1
                start_index+=1
                res = max(res,count)
            else:
                count-=1
                end_index+=1
        return res