class Solution:
    def replaceElements(self, arr: List[int]) -> arr[int]:
        # O(N)
        l = len(arr)
        currentMax = -1
        for i in range(l-1,-1,-1):
            original = arr[i]
            arr[i] = currentMax
            currentMax = max(original,currentMax)
        return arr

        # O(N^2)
        # l = len(arr)
        # for i in range(l):
        #     if(i==l-1):
        #         arr[i]=-1
        #         break
        #     arr[i] = max(arr[i+1:l])
        # return arr