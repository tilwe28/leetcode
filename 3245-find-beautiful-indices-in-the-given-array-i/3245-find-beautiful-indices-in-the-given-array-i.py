class Solution:
    def KMP(self, h: str, n: str) -> List[int]:
        # LPS for needle
        lps = [0] * len(n)
        prevLPS, i = 0, 1
        while i < len(n):
            if n[i] == n[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        # KMP for needle
        indices = []
        h_ptr, n_ptr = 0, 0
        while h_ptr < len(h):
            if h[h_ptr] == n[n_ptr]:
                h_ptr += 1
                n_ptr += 1

                if n_ptr == len(n):
                    indices.append(h_ptr - len(n))
                    h_ptr -= (len(n) - 1)
                    n_ptr = 0

            elif n_ptr == 0:
                h_ptr += 1
            else:
                n_ptr = lps[n_ptr - 1]

        return indices


    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        indices_a = self.KMP(s, a)
        indices_b = self.KMP(s, b)

        res = []
        ap, bp = 0, 0
        while ap < len(indices_a) and bp < len(indices_b):
            idx_a, idx_b = indices_a[ap], indices_b[bp]
            if idx_a - k <= idx_b <= idx_a + k:
                res.append(idx_a)
                ap += 1
            elif idx_a < idx_b:
                ap += 1
            else:
                bp += 1

        return res
        
"""
1. i <= (len(s) - len(a))
    - otherwise a won't fit at starting index
2. i is the starting index such that s[i] to s[i + len(a) - 1] == a
    - a is a substring of s at this index
3. there exists another index j but with string b as a substring of s
    - |j - i| <= k

find all such indices i

INITIAL THOUGHTS:
- iterate through all indices (0 to len(s) - len(a))
- check if condition 2 is satisfied
    - if so, repeat for another index j
- continue for all indices
Time: O(n^2)
Space: O(n)

OPTIMIZATIONS:
- use KMP algorithm to find indices of substring a and substring b in s
- setup LPS for str a and str b
- find indices for matches (i for a, j for b)
- filter indices i such that |i - j| <= k
    - 2 pointer
Time: O(n)
Space: O(n)
"""