'''You are given two 2D integer arrays nums1 and nums2.
nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

Example 2:
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
 '''

#code 1
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        n1=0
        n2=0
        res=[]
        while n1!=len(nums1) and n2!=len(nums2):
            if nums1[n1][0]<nums2[n2][0]:
                idx=nums1[n1][0]
                psum=nums1[n1][1]
                n1+=1
            elif nums1[n1][0]==nums2[n2][0]:
                idx=nums1[n1][0]
                psum=nums1[n1][1]+nums2[n2][1]
                n1+=1
                n2+=1
            else:
                idx=nums2[n2][0]
                psum=nums2[n2][1]
                n2+=1
            res.append([idx,psum])
            psum=0
        while n1!=len(nums1):
            res.append([nums1[n1][0],nums1[n1][1]])
            n1+=1
        while n2!=len(nums2):
            res.append([nums2[n2][0],nums2[n2][1]])
            n2+=1
        return res


            
#code 2

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = dict()

        for num in nums1:
            if num[0] in temp:
                temp[num[0]] += num[1]
            else:
                temp[num[0]] = num[1]
        for num in nums2:
            if num[0] in temp:
                temp[num[0]] += num[1]
            else:
                temp[num[0]] = num[1]
        res = []
        for i in temp.keys():
            res.append([i,temp[i]])
        return sorted(res)