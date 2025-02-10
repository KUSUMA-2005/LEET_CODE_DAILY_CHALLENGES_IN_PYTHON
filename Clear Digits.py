'''You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""'''



class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for c in s:
            if c.isdigit():
                if res:
                    res = res[:-1]  
            else:
                res += c  
        return res