class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1_idx = [i for i, w in enumerate(wordsDict) if w == word1]
        w2_idx = [i for i, w in enumerate(wordsDict) if w == word2]
        w1_idx.sort()
        w2_idx.sort()
        print(w1_idx)
        print(w2_idx)
    
        min_dist = len(wordsDict)
        p1, p2 = 0, 0

        while p1 < len(w1_idx) and p2 < len(w2_idx):
            i, j = w1_idx[p1], w2_idx[p2]
            if i == j:
                if p1 <= p2:
                    p1 += 1
                else:
                    p2 += 1
                continue

            min_dist = min(min_dist, abs(i - j))
            if i < j:
                p1 += 1
            else:
                p2 += 1

        while p1 < len(w1_idx):
            i = w1_idx[p1]
            j = w2_idx[-1]

            if i == j:
                p1 += 1
                continue

            min_dist = min(min_dist, abs(i - j))
            p1 += 1

        while p2 < len(w2_idx):
            i = w1_idx[-1]
            j = w2_idx[p2]

            if i == j:
                p2 += 1
                continue

            min_dist = min(min_dist, abs(i - j))
            p2 += 1

        return min_dist


"""
BRUTE FORCE:
- iterate through dict
- track min distacnce between word1 and word2
Time: O(n^2)
Space: O(1)

INITIAL THOUGHTS:
- iterate over dict, track indices for word1
- iterate over dict, track indices for word2
- find min difference*
    - sort arrays
    - use 2 pointer approach to find min
Time: O(n log n)
Space: O(n)
"""