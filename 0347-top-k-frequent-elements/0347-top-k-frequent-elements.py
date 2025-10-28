class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            buckets[c].append(n)
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                res.append(n)
            if len(res) == k:
                return res

"""
- count frequency of each num
- create buckets for each frequency (list of lists)
- add numbers in highest frequency until k added
"""