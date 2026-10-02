import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max-heap via negated distances
        for x, y in points:
            d = x * x + y * y          # skip sqrt; ordering is preserved
            heapq.heappush(heap, (-d, x, y))
            if len(heap) > k:
                heapq.heappop(heap)    # removes the farthest point
        return [[x, y] for _, x, y in heap]   # <- the return you're likely missing