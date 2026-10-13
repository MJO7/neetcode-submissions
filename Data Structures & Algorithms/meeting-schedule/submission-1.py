"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals_list = []
        for interval in intervals:
            intervals_list.append([interval.start,interval.end])
        intervals_list.sort(key = lambda i : i[0])
        i = 1
        while i < len(intervals_list):
            if intervals_list[i-1][1]>intervals_list[i][0]:
                return False
            i = i+1
        return True