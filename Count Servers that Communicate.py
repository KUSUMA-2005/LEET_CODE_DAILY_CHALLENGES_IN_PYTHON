# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        count=0
        rc=[0]*m
        cc=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rc[i]+=1
                    cc[j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rc[i]>1 or cc[j]>1):
                    count+=1
        return count

# Problem:
# We have a grid where each cell is either a 1 (server) or 0 (no server). We need to count how many servers can communicate with at least one other server, either in the same row or column.

# Approach:
# Count servers in each row and column:
    # Use two arrays rc (for rows) and cc (for columns) to store the number of servers in each row and column.
# Identify communicative servers:
    # Iterate through the grid again, and for each server, check if there's another server in its row or column (rc[i] > 1 or cc[j] > 1).
# Return the count of communicative servers.