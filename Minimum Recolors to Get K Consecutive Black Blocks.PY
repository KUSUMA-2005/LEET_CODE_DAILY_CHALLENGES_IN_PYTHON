'''You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
'
'Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.'''


#SOLUTION 1

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        ans=float("inf")
        p=0
        while p<len(blocks)-k+1:
            count=0
            count_w=0
            for i in range(p,len(blocks)):
                if blocks[i]=="W":
                    count_w+=1
                count+=1
                if count==k:
                    ans=min(ans,count_w)
                    break
            p+=1
        return ans
        
#SOLUTION 2
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        present_count_B=[0]*len(blocks)
        if blocks[0]=="B":
            present_count_B[0]=1 
        for i in range(1,len(blocks)):
            present_count_B[i]=present_count_B[i-1]+1 if blocks[i]=="B" else present_count_B[i-1]
        
        p1=0
        j=0
        ans=float("inf")
        for i in range(k-1,len(present_count_B)):
            ans=min(ans,k+p1-present_count_B[i])
            p1=present_count_B[j]
            j+=1
        return ans
    
#SOLUTION 3

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        count_w=blocks[:k].count("W")
        ans=count_w
        for i in range(k,len(blocks)):
            if blocks[i - k]=="W":
                count_w-=1
            if blocks[i]=="W": 
                count_w+= 1
            ans=min(ans,count_w)
        return ans