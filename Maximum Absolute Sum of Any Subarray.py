'''You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.'''

#code 1
class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = 0
        min_sum = 0
        cur_max = 0
        cur_min = 0
        
        for num in nums:
            cur_max = max(num,cur_max + num) 
            cur_min = min(num, cur_min + num)  
            max_sum = max(max_sum, cur_max)    
            min_sum = min(min_sum, cur_min)    
        return max(max_sum, abs(min_sum))  
    
    
#code 2
class Solution(object):
    def maxAbsoluteSum(self, nums):
        s=0
        max_sum=0
        min_sum=0
        for num in nums:
            s+=num
            max_sum=max(max_sum,s)
            min_sum=min(min_sum,s)
        return max_sum-min_sum

