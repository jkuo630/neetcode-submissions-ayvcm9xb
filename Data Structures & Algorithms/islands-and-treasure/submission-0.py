class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # iterate through grid, adding treasure chests to bfs queue 
        # start multi wave bfs, tracking each wave of bfs, changing its
        # neighbours 

        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        # add treasure chests 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647):                        
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        