class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        
        while n > 9:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            n = sum([digit ** 2 for digit in digits])

        return n == 1 or n == 7