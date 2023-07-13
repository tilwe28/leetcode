class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            merged += word1[i] + word2[i]
        if len(word1) > len(word2):
            merged += word1[len(word2):]
        elif len(word1) < len(word2):
            merged += word2[len(word1):]
        return merged