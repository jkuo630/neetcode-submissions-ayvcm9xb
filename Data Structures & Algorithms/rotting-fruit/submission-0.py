class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten fruits, add it to the queue 
        # track total fruits, time and rotten fruits 
        # if total fruits == rotten fruits at the end, return time 
        # increment time after each bfs wave
        # else, return -1 

        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        rotten_fruit = 0
        total_fruit = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    rotten_fruit += 1
                    total_fruit += 1 
                elif grid[r][c] == 1:
                    total_fruit += 1 
        
        time = 0 

        while q and rotten_fruit < total_fruit:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if(
                        (r + dr) in range(rows) and 
                        (c + dc) in range(cols) and 
                        grid[r+dr][c+dc] == 1
                    ):
                        grid[r+dr][c+dc] = 2
                        q.append((r + dr, c + dc))
                        rotten_fruit += 1
            
            time += 1 

        if rotten_fruit == total_fruit:
            return time 
        else:
            return -1