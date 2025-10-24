class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        curr = x
        rev = 0
        while curr:
            rev *= 10
            rev += (curr % 10)
            curr //= 10
        return rev == x