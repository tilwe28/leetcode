class Solution:
    def KMP(self, txt: str, pat: str) -> List[int]:
        lps = [0] * len(pat)
        i, prevLPS = 1, 0
        while i < len(pat):
            if pat[i] == pat[prevLPS]:
                prevLPS += 1
                lps[i] = prevLPS
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        indices = []
        txt_p, pat_p = 0, 0
        while txt_p < len(txt):
            if txt[txt_p] == pat[pat_p]:
                txt_p += 1
                pat_p += 1

                if pat_p == len(pat):
                    indices.append(txt_p - len(pat))
                    pat_p = lps[pat_p - 1]

            elif pat_p == 0:
                txt_p += 1
            else:
                pat_p = lps[pat_p - 1]

        return indices

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        indices_a = self.KMP(s, a)
        indices_b = self.KMP(s, b)

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