'''Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1'''

#code 1
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        ans=0
        abc_count=Counter()
        for right in range(left,len(s)):
            if s[right] in "abc":
                abc_count[s[right]]+=1
            while len(abc_count)==3 and all(abc_count.values()):
                ans+=len(s)-right
                if s[left] in "abc":
                    abc_count[s[left]]-=1
                if abc_count[s[left]]==0:
                    del abc_count[s[left]]
                left+=1
        return ans
            

#code 2
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        count = [0, 0, 0]  
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1 
            while all(count):
                ans += len(s) - right
                count[ord(s[left]) - ord('a')] -= 1 
                left += 1
        return ans
            

#code 3

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        count=[-1,-1,-1]
        for i,c in enumerate(s):
            count[ord(c)-97]=i
            ans+=min(count)+1
        return ans
        