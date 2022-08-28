class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # number of rows
        rows = len(grid)
        if rows == 0:
            return -1
        
        # number of cols
        cols = len(grid[0])
        
        # count of fresh oranges
        fresh_cnt = 0
        
        # queue storing rotten oranges
        rotten = deque()
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # count the number of fresh oranges
                    fresh_cnt += 1
        
        # count of minutes passed
        minutes_cnt = 0
        
        while fresh_cnt and rotten:
            
            minutes_cnt += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue

                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    fresh_cnt -= 1

                    grid[xx][yy] = 2

                    rotten.append((xx, yy))
                
        return minutes_cnt if not fresh_cnt else -1