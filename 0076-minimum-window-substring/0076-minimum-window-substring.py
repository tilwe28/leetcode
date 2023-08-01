class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str = ""
        countT, countCurr = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l, r = 0, 1
        countCurr[s[0]] = 1
        while l != len(s):
            curr = s[l:r]
            isValid = True
            for c in countT:
                if countCurr.get(c, 0) < countT[c]:
                    isValid = False
                    break
            if isValid and (len(curr) < len(min_str) or min_str == ""):
                min_str = curr
            if isValid and l < r:
                countCurr[s[l]] -= 1
                l += 1
            elif r < len(s):
                countCurr[s[r]] = 1 + countCurr.get(s[r], 0)
                r += 1
            else:
                countCurr[s[l]] -= 1
                l += 1
        return min_str

"""
SLIDING WINDOW

~ iterate through string with window and check condition
~ the condition is that every character in t is in the curr substring (including duplicates)
~ to check condition, have charCount for t and curr substring, and every count in t must be <= the corresponding count in curr substring
~ have a substring based on length and update if condition is met
~ if condition is not met, make window bigger first from right pointer, then from left
~ return min substring



curr = "DOBEC"

"""