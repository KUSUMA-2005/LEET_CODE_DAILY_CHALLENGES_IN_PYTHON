'''You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".'''

class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        def helper(k):
            ans = 0
            left = 0
            vowel_count = Counter()  
            consonant_count = 0 
            for right in range(n):
                if word[right] in 'aeiou':
                    vowel_count[word[right]] += 1  
                else:
                    consonant_count += 1
                while len(vowel_count) == 5 and consonant_count >= k:
                    ans += (n - right)  
                    if word[left] in 'aeiou':
                        vowel_count[word[left]] -= 1
                        if vowel_count[word[left]] == 0:
                            del vowel_count[word[left]]  
                    else:
                        consonant_count -= 1 
                    left += 1 
            return ans
        return helper(k) - helper(k + 1)
