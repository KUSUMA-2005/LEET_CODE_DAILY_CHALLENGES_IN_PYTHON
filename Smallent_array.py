'''You are given a 0-indexed array of positive integers nums and a positive integer limit.
In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.
Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.
Example 1:
Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.'''


class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        if n == 0:
            return []
        sorted_pairs=sorted([(nums[i],i) for i in range(n)])
        res=[0]*n
        group_start=0
        for i in range(n):
            if i==n-1 or sorted_pairs[i+1][0]-sorted_pairs[i][0]>limit:
                indices=[pair[1] for pair in sorted_pairs[group_start:i+1]]
                indices.sort()
                for j in range(len(indices)):
                    res[indices[j]]=sorted_pairs[group_start+j][0]
                group_start=i+1
        return res
                
'''This solution aims to transform the input array nums into its lexicographically smallest form within the given limit.
Steps:
    Sorting pairs: The array nums is paired with its indices and sorted based on the values.
    Grouping and Updating: It traverses through the sorted pairs, grouping consecutive values that differ by more than limit (i.e., they can't be adjusted to form a lexicographically smaller result). For each group, the values are placed in ascending order by their original indices.
    Final Result: After all groups are processed, the resulting array res holds the lexicographically smallest possible arrangement.
Key Concepts:
    Sorting helps in identifying the smallest possible values.
    The limit ensures values in each group are close enough to be swapped or adjusted.'''