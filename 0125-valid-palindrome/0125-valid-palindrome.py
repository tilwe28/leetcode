class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        condensed = ""
        for c in s:
            if c.isalnum():
                condensed += c.lower()
        for i in range(len(condensed)):
            if condensed[i] != condensed[(i+1)*-1]:
                return False
        return True

        O(n) time complexity
        O(n) space complexity
        """

        # Better solution (technically)
        def alnum(c: str):
            return (
                ord('A') <= ord(c) <= ord('Z')
                or ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9')
            )

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not alnum(s[l]):
                l += 1
            while l < r and not alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # O(n) time complexity
        # O(1) space complexity