class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for u, v, w in times:
            adjList[u].append([v, w])
        minHeap = [(0, k)]
        visit = set()
        res = 0
        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = w
            for v2, w2 in adjList[node]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w2 + w, v2))
        return res if len(visit) == n else -1
