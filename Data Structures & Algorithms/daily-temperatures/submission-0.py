class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp,index]
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                newTemp,newIndex = stack.pop()
                res[newIndex] = (i-newIndex)
            stack.append([t,i])
            
        return res

