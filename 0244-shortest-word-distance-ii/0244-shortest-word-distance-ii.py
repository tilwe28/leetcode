class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.map = defaultdict(list)
        self.max = len(wordsDict)
        for i, word in enumerate(wordsDict):
            self.map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = self.max
        i2 = 0
        for idx1 in self.map[word1]:
            while i2 < len(self.map[word2]):
                idx2 = self.map[word2][i2]
                res = min(res, abs(idx1 - idx2))

                if idx2 > idx1:
                    break

                i2 += 1
        return res

"""
initial thoughts:
during initialization, have a map of word to list of indices
for one word, indices will be in order
on query, compare pairs of indices and return min distance

for each index of word1
    iterate through indices of word2
    after the first instance where idx2 > idx1 stop
"""

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)