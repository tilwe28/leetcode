class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        indices_a = []
        for i in range(len(s) - len(a) + 1):
            if s[i:len(a) + i] == a:
                indices_a.append(i)

        indices_b = []
        for i in range(len(s) - len(b) + 1):
            if s[i:len(b) + i] == b:
                indices_b.append(i) 

        res = []
        ap, bp = 0, 0
        while ap < len(indices_a) and bp < len(indices_b):
            idx_a, idx_b = indices_a[ap], indices_b[bp]
            if abs(idx_b - idx_a) <= k:
                res.append(idx_a)
                ap += 1
            elif idx_a < idx_b:
                ap += 1
            else:
                bp += 1

        return res