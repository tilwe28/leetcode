class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)
        self.min = sys.maxsize
        self.max = -sys.maxsize

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1
        self.min = min(self.min, timestamp)
        self.max = max(self.max, timestamp)

    def getHits(self, timestamp: int) -> int:
        res = 0
        for time in range(max(self.min, timestamp - 300 + 1), min(self.max, timestamp) + 1):
            if time not in self.hits:
                continue
            res += self.hits[time]
        return res

"""
idea:
- have a map of timestamp to number of hits
"""


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)