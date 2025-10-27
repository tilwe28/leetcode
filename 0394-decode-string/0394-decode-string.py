class Solution:
    def decodeSubString(self, s: str) -> (str, int):
        res = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                res += s[i]
            elif s[i].isdigit():
                j = s[i:].find('[')
                k = int(s[i:i+j])
                substr, i_inc = self.decodeSubString(s[i+j+1:])
                res += substr * k
                i = i + j + i_inc + 1
            elif s[i] == ']':
                return res, i
            i += 1

    def decodeString(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                res += s[i]
            elif s[i].isdigit():
                j = s[i:].find('[')
                k = int(s[i:i+j])
                substr, i_inc = self.decodeSubString(s[i+j+1:])
                res += substr * k
                i = i + j + i_inc + 1
            i += 1
        
        return res
            

"""
result string
for normal characters, just add it to the result
if a number digit is seen, then get the number by taking the substring from the first digit until the opening bracket
- i = idx of digit, j = s[i:].find('['), k = int(s[i:j])
- e = s[j:].find(']'), encoded_substr = s[j+1:e]
- res += encoded_substr * k

problem with above, it doesn't account for nested encodings
- use a helper function that is called when an encoding is seen
- return from the encoding when a ']' is seen
"""