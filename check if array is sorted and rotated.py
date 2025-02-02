'''Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.'''

#method 1
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=sorted(nums)
        for x in range(len(nums)):
            flag=True
            for i in range(len(nums)):
                if a[i]!=nums[(i+x) % len(a)]:
                    flag=False
            if flag==True:
                return True
        return False
                    
#method 2
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count,n=0,len(nums)
        if n <= 1:
            return True
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
            if count>1:
                return False
        return True