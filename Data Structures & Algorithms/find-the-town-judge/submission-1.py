class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_edges = collections.defaultdict(int)
        outgoing_edges = collections.defaultdict(int)
        for i,j in trust:
            outgoing_edges[i]+=1
            incoming_edges[j]+=1
        for i in range(1,n+1):
            if outgoing_edges[i]==0 and incoming_edges[i]==n-1:
                return i
        return -1