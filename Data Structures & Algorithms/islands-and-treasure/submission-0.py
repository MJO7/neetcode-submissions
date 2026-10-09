class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    queue.append((i,j))
                    visit.add((i,j))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance #because we need to have shortest distance to nearby treasure on each land cell.
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr,dc in directions:
                    if ((r+dr)<0 or (c+dc)<0 or (r+dr)==ROWS or (c+dc)==COLS
                    or ((r+dr,c+dc) in visit) or grid[r+dr][c+dc] == -1):
                        continue
                    else:
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
            distance+=1

                    


