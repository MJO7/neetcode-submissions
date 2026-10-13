class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])       
        res = []
        res.append(intervals[0])
        res_index = 0
        index =1
        while index<len(intervals):
            if res[res_index][1] >= intervals[index][0]:
                res[res_index][1] = max(res[res_index][1],intervals[index][1])
                index=index + 1
            else:
                res.append(intervals[index])
                res_index = res_index+1
                index+=1
        return res