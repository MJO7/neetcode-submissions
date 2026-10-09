class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if (grid[0][0]==1 or grid[n-1][n-1]==1):
            return -1

        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))
        length = 1 #because even the starting cell counts as one 

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                if r==n-1 and c==n-1:
                    return length 

                directions = [[1,0],[-1,0],[0,1],[0,-1],
                                [1,1],[-1,-1],[-1,1],[1,-1]]
                for dr,dc in directions:
                    if (min(r+dr, c+dc)<0 or max(r+dr,c+dc)==n or 
                    ((r+dr,c+dc) in visit) or grid[r+dr][c+dc]==1):
                        continue
                    else:
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
            
            length+=1

        return -1
        
                
                