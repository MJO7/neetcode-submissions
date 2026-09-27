class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countMap1 = defaultdict(int)
        countMap2 = defaultdict(int)
        for i in s1:
            countMap1[i]+=1

        left = 0
        right = len(s1)-1
        while right<len(s2):
            for index in range(left,right+1):
                countMap2[s2[index]]+=1
            if countMap2==countMap1:
                return True
            else:
                left+=1
                right+=1
                countMap2.clear()
        return False