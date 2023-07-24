class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlnum(c: str):
            return (
                ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9')
            )

        """
        # method 1
        condensed = ""
        for c in s:
            if isAlnum(c):
                condensed += c.lower()
        l, r = 0, len(condensed) - 1
        while l < r:
            if condensed[l] != condensed[r]:
                return False
            l += 1
            r -= 1
        return True

        # O(n) time
        # O(n) space
        """

        # method 2
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlnum(s[l]):
                l += 1
            while l < r and not isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # O(n) time
        # O(1) space