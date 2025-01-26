# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:
# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

# Example 1:
# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]

# Example 2:

# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(isWater)
        m = len(isWater[0])
        height = [[-1] * m for _ in range(n)]
        queue=deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j]==1:
                    height[i][j]=0
                    queue.append((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            i,j=queue.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<n and 0<=nj<m and height[ni][nj]==-1:
                    height[ni][nj]=height[i][j]+1
                    queue.append((ni,nj))
        return height

# Explanation:
# The function initializes a grid height where each cell is initially set to -1 to represent unexplored cells.
# It uses a breadth-first search (BFS) starting from all water cells (cells with 1) to calculate the minimum distance to a water cell for each land cell (cells with 0).
# A queue is used for the BFS, and as the BFS progresses, it updates the heights of the land cells with increasing values depending on their distance from the nearest water cell.
# The algorithm ensures that the height of the land cells increases as we move away from the water cells, providing the highest peaks.

# Steps:
# Initialize a height matrix with all values set to -1.
# Enqueue all water cell coordinates and set their height to 0.
# Perform BFS, updating the height of each adjacent land cell.
# Return the updated height matrix.
# This approach runs efficiently with a time complexity of O(n * m), where n is the number of rows and m is the number of columns in the grid.
