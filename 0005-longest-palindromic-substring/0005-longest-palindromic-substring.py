class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx:resIdx+resLen]

"""
initial thoughts:
brute force is to check every substring
O(n^2) substrings and O(n) to check palindrome
total runtime of O(n^3)

for each char, check if there's a valid palindrome with center starting from there
track longest
"""