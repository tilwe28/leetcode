class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = len(wordsDict)
        prev_idx = -1
        is_same = word1 == word2

        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if prev_idx != -1 and (is_same or word != wordsDict[prev_idx]):
                    min_dist = min(min_dist, i - prev_idx)
                prev_idx = i

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

Optimal:
- iterate through dict
- track index of prev word (word1 or word2)
    - flag for if word1 == word2
- track min_dist
Time: O(n)
Space: O(1)
"""