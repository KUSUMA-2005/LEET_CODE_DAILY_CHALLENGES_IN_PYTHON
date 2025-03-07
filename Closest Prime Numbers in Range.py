'''Given two positive integers left and right, find the two integers num1 and num2 such that:
left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:
Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.'''

#code 1
class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(math.sqrt(n)) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
        ans = [-1, -1]
        prev_prime = -1  
        if left <= 2 and right >= 2:
            prev_prime = 2
            left = 3 
        for i in range(left, right + 1, 2 if left % 2 != 0 else 1):  
            if is_prime(i):
                if prev_prime != -1:
                    if ans == [-1, -1] or (i - prev_prime < ans[1] - ans[0]):
                        ans = [prev_prime, i]
                prev_prime = i  
        return ans


#code 2

class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False 
            for i in range(2, int(math.sqrt(n)) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime
        prime_flags = sieve(right)
        primes = [i for i in range(left, right + 1) if prime_flags[i]]
        if len(primes) < 2:
            return [-1, -1]
        min_diff = float('inf')
        ans = [-1, -1]
        for j in range(len(primes) - 1):
            diff = primes[j + 1] - primes[j]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[j], primes[j + 1]]
        return ans
