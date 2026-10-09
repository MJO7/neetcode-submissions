class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS =  len(grid)
        COLS = len(grid[0])
       
        queue = deque()

        fresh_fruit_remaining = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh_fruit_remaining+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
                   
        if fresh_fruit_remaining==0:
            return 0

        minutes_passed = 0
        
        while queue and fresh_fruit_remaining>0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
               
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if ((r+dr)<0 or (c+dc)<0 or (r+dr)==ROWS or c+dc==COLS 
                    or grid[r+dr][c+dc]==0):
                        continue
                    elif grid[r][c]==2 and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc] = 2
                        fresh_fruit_remaining-=1
                        queue.append((r+dr,c+dc))
                     

            minutes_passed+=1
        
        return minutes_passed if fresh_fruit_remaining == 0 else -1
                    

