"""Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 """


#code 1
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        zero_count=0
        count=0
        i=0
        while i<n and nums[i]<=0:
            if nums[i]<0:
                count+=1
            else:
                zero_count+=1
            i+=1
        return max(count,(n-count-zero_count))


#code 2
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count=bisect_left(nums,0)
        pos_count=len(nums)-bisect_right(nums,0)
        return max(neg_count,pos_count)
                