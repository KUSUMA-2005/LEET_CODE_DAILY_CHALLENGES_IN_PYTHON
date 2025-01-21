# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
# Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
# At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.
# The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.


class Solution:
    def gridGame(self, grid):
        n = len(grid[0])  
        pref1,pref2=grid[0][:], grid[1][:]
        for i in range(1,n):
            pref1[i]+=pref1[i-1]
            pref2[i]+=pref2[i-1]
        res=float("inf")
        for i in range(n):
            top=pref1[-1]-pref1[i]
            bottom=0 if i==0 else pref2[i-1]
            res=min(res,max(top,bottom))
        return res


# The problem involves finding the optimal point to split the grid such that the second robot's maximum collected coins are minimized. This can be achieved by analyzing prefix sums and evaluating the worst-case scenarios for each potential split point.

# Approach
# Compute prefix sums for both rows (pref1 and pref2) to quickly calculate the sum of coins in any segment of a row.
# For each possible split point i, calculate:
# The remaining coins in the top row (top), starting from the split point.
# The collected coins in the bottom row (bottom), ending at the split point.
# Determine the maximum of these two values for each split point.
# Minimize this maximum value across all split points to ensure the second robot is left with the least disadvantage.
# Return the minimized value as the result.