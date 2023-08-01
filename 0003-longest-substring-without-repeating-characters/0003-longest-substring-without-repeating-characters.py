class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, max_len = 0, 0
        for i,c in enumerate(s):
            while c in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(c)
            max_len = max(max_len, i-l+1)
        return max_len