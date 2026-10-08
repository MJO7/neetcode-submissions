class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        visit = set()


        def dfs(r,c):
            if (r<0 or r>=m or c<0 or c>=n or grid[r][c]==0 or ((r,c) in visit)):
                return 0

            visit.add((r,c))
            return(1+dfs(r+1,c)+
            dfs(r-1,c)+
            dfs(r,c+1)+
            dfs(r,c-1))
            

        max_area = 0
        for r in range(m):
            for c in range(n):
                max_area = max(dfs(r,c), max_area)

        return max_area
                
