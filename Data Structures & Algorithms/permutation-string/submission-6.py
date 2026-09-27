class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        countMap1 = defaultdict(int)
        for i in s1:
            countMap1[i]+=1
        countMap2 = defaultdict(int)

        left = 0
        # making the first window
        for j in range(0,len(s1)):
            countMap2[s2[j]]+=1

        if countMap1==countMap2:
            return True

        # now moving the sliding window forward throughout s2
        for right in range(len(s1),len(s2)):
            leavingChar = s2[left]
            countMap2[leavingChar]-=1
            if countMap2[leavingChar]==0:
                del countMap2[leavingChar] 
            left+=1
            
            countMap2[s2[right]]+=1
            
            if countMap1==countMap2:
                return True

        return False