class Solution:
    def partitionString(self, s: str) -> List[str]:
        res = []
        seen = set()
        l = 0
        while l < len(s):
            r = l + 1
            while r <= len(s):
                if s[l:r] not in seen:
                    res.append(s[l:r])
                    seen.add(s[l:r])
                    l = r - 1
                    break
                r += 1
            l += 1
        return res