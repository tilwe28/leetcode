class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        i = 0
        while i < len(s):
            num = symbols[s[i]]
            if i + 1 < len(s) and s[i] in "IXC" and s[i + 1] in "VXLCDM":
                if (s[i] == "I" and s[i + 1] in "VX") or \
                    (s[i] == "X" and s[i + 1] in "LC") or \
                    (s[i] == "C" and s[i + 1] in "DM"):
                    num = symbols[s[i + 1]] - symbols[s[i]]
                    i += 1
            res += num
            i += 1
        
        return res
