"""You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54."""

#SOLUTION-1
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_arr = [0] * 82
        ans = -1
        for x in nums:
            digit_sum = sum(int(d) for d in str(x))
            if max_arr[digit_sum] != 0:
                ans = max(ans, x + max_arr[digit_sum])
            max_arr[digit_sum] = max(max_arr[digit_sum], x)
        return ans
    
#SOLUTION-2

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-1
        num_map={}
        for num in nums:
            digit_sum=sum(int(digit) for digit in str(num))
            if digit_sum in num_map:
                ans=max(ans,num_map[digit_sum]+num)
            num_map[digit_sum]=max(num_map.get(digit_sum,0),num)
        return ans