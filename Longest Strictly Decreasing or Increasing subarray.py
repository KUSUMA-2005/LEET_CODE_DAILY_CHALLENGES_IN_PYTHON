'''You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.'''  

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans=1
        decreasing=1
        increasing=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increasing+=1
                decreasing=1
            elif nums[i]<nums[i-1]:
                decreasing+=1
                increasing=1
            else:
                increasing=decreasing=1
            ans=max(ans,decreasing,increasing)
        return ans
            