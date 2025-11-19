class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def decode() -> str:
            nonlocal i
            res = []
            k = []
            while i < len(s):
                if s[i].isdigit():
                    k.append(s[i])
                    i += 1
                elif s[i] == '[':
                    i += 1
                    res.append(decode() * int(''.join(k)))
                    k = []
                elif s[i] == ']':
                    i += 1
                    return ''.join(res)
                else:
                    res.append(s[i])
                    i += 1
            
            return ''.join(res)

        return decode()

"""
initial thoughts:
- iterate through the string
- different cases of the character
    - digit
    - letter
    - opening bracket
    - closing bracket
- if digit
    - continue reading the number until '['
- if opening bracket '['
    - call helper function, append output * k
- if closing bracket ']'
    - return output
- if letter
    - keep appending to output
"""