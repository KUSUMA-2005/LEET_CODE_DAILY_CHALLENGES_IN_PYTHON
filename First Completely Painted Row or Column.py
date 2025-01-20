# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])  
        painted_rows = [0] * m 
        painted_cols = [0] * n
        position_map={}
        for i in range(m):
            for j in range(n):
                position_map[mat[i][j]]=(i,j)
        for idx,num in enumerate(arr):
            i,j=position_map[num]
            painted_rows[i]+=1
            painted_cols[j]+=1
            if painted_rows[i]==n or painted_cols[j]==m:
                return idx
        return -1
    

#     This solution uses a greedy approach to keep track of which rows and columns are completed as numbers from arr are processed. It efficiently determines the first index where a row or column gets fully painted (i.e., where all its numbers have appeared in arr).
# Steps:
# Input Definitions:
    # arr: A list of integers where the goal is to mark numbers and check if a row or column in mat is completed.
    # mat: A 2D list (matrix) representing the grid. We need to track if any row or column in this matrix becomes fully painted by numbers appearing in arr.
# Initial Setup:
    # m and n are the dimensions of the matrix mat, where m is the number of rows and n is the number of columns.
    # painted_rows is a list of length m initialized to 0. Each entry in this list tracks how many numbers from arr have appeared in that row.
    # painted_cols is a list of length n initialized to 0. Each entry in this list tracks how many numbers from arr have appeared in that column.
    # position_map is a dictionary that maps each number in mat to its position (row, column).
# Position Mapping:
    # We iterate over all elements in mat and store each element's coordinates (i, j) in the position_map. This allows us to quickly find where each number appears in the matrix.
# Processing arr:
    # We then iterate through arr, and for each number, we:
    # Look up the position of the number in mat using position_map.
    # Increment the corresponding row and column in painted_rows and painted_cols.
    # Check if any row or column has been completely painted:
    # A row is considered fully painted if all of its columns have been marked (i.e., painted_rows[i] == n).
    # A column is considered fully painted if all of its rows have been marked (i.e., painted_cols[j] == m).
    # If either a row or a column is fully painted, return the index of the current number in arr.
# Return -1:
    # If no row or column is completely painted by the time we process all numbers in arr, return -1.
