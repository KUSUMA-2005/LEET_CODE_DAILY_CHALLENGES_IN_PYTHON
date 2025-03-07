'''You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Example 1:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

Example 2:
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
 '''

#solution 1

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        seen = {i: 0 for i in range(1,(n**2)+1)}
        for i in range(n):
            for j in range(n):
                seen[grid[i][j]]+=1
        for i in range(1,(n**2)+1):
            if seen[i]==0:
                missing=i
            if seen[i]==2:
                rep=i 
        return [rep,missing]
                

#solution 2
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid) 
        lst = [num for row in grid for num in row]
        sum_n = n**2 * (n**2 + 1) // 2
        sum_squares = n**2 * (n**2 + 1) * (2 * n**2 + 1) // 6
        grid_sum = sum(lst)
        grid_sum_squares = sum(num * num for num in lst)
        diff_sum = grid_sum - sum_n  
        diff_sum_squares = grid_sum_squares - sum_squares
        sum_ab = diff_sum_squares // diff_sum  
        a = (diff_sum + sum_ab) // 2
        b = (sum_ab - diff_sum) // 2
        return [a, b]


