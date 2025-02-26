"""Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
"""

#code 1
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix_sum = 0
        odd_sum = 0
        mod = 10**9 + 7
        for val in arr:
            prefix_sum += val
            odd_sum += prefix_sum % 2
        odd_sum += (len(arr) - odd_sum ) * odd_sum
        return odd_sum % mod
    
#code 2


class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  
        prefix_sum = 0
        count = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count = (count + odd_count) % MOD
                even_count += 1
            else:
                count = (count + even_count) % MOD
                odd_count += 1
        return count
    