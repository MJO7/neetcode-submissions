# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        each_output = []

        for i in range(len(pairs)):
            j = i-1
            while j>=0 and pairs[j+1].key<pairs[j].key:
                pairs[j],pairs[j+1] = pairs[j+1],pairs[j]
                j-=1
            each_output.append(pairs[:])        #cloning as it only saves reference to the same list object otherwise
            #it also comes OUTSIDE of the while loop not inside.

        return each_output