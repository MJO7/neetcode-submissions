class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        minHeap =[]
        for i in count.keys():
            heapq.heappush(minHeap,(count[i],i))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res