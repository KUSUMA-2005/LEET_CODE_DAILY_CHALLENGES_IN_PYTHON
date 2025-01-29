'''You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:
Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.'''

#USING DFS

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        max_fish = 0
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            fish_count = grid[r][c]
            grid[r][c] = 0
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    fish_count += dfs(nr, nc) 
            return fish_count
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  
                    max_fish = max(max_fish, dfs(r, c))  
        return max_fish

# USING BFS
from collections import deque

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_count = 0
        
        def bfs(r, c):
            fish_count = grid[r][c]
            grid[r][c] = 0
            queue = deque([(r, c)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    nr, nc = x + dx, y + dy
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                        fish_count += grid[nr][nc]
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return fish_count
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_count = max(max_count, bfs(r, c))
        return max_count



