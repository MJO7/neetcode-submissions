class Solution:
    def replaceElements(self, arr: List[int]) -> arr[int]:
        l = len(arr)
        for i in range(l):
            if(i==l-1):
                arr[i]=-1
                break
            arr[i] = max(arr[i+1:l])
        return arr