class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        my_dict = defaultdict(int)
        for i in nums:
            my_dict[i]+=1
        sorted_list = sorted(my_dict.items(),key = lambda x : x[1])
        for i in range(len(sorted_list)-1,len(sorted_list)-1-k,-1 ):
            out.append(sorted_list[i][0])
        return out
        