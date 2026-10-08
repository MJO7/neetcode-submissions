class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        no_of_islands = 0

        def dfs(r,c):
            if (r<0 or r>=m or c<0 or c>=n or grid[r][c]=='0'):
                return '0'

            grid[r][c]='0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    dfs(r,c)    #this goes ahead and finds the whole ass island lol
                    no_of_islands+=1

        return no_of_islands

        
            
            
            