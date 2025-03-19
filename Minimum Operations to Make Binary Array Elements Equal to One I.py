'''You are given a binary array nums.
You can do the following operation on the array any number of times (possibly zero):
Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.
Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

Example 1:
Input: nums = [0,1,1,1,0,0]
Output: 3
Explanation:
We can do the following operations:
Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

Example 2:
Input: nums = [0,1,1,1]
Output: -1
Explanation:
It is impossible to make all elements equal to 1.'''

#code 1

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        l=0
        for i in range(len(nums)-2):
            r=l+2
            if nums[i]==0:
                for j in range(l,r+1):
                    nums[j]=abs(1-nums[j])
                count+=1
            l+=1
        return count if sum(nums)==len(nums) else -1
        


#code 2

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        l=0
        for idx,value in enumerate(nums):
            if value==0:
                if idx+2>=len(nums):
                    return -1
                nums[idx+1]^=1
                nums[idx+2]^=1
                count+=1
        return count 
        


            

