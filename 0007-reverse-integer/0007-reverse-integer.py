class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        digits = []
        while x:
            digits.append(x % 10)
            x //= 10
        
        res = 0
        for digit in digits:
            res = (res * 10) + digit
        
        return sign * res if res <= 2**31 - 1 else 0

"""
initial thoughts:
- have a list of digits
- get the last digit and add to list
- order of digits in list is reverse of original
- for each digit in list multiply res * 10 + digit
"""