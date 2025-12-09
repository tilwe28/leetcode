class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        for w in words1:
            counts1[w] += 1
        for w in words2:
            counts2[w] += 1
        
        res = 0
        m1 = counts1 if len(counts1) <= len(counts2) else counts2
        m2 = counts1 if len(counts1) > len(counts2) else counts2
        for w, c in m1.items():
            if c == 1 and w in m2 and m2[w] == 1:
                res += 1
        
        return res