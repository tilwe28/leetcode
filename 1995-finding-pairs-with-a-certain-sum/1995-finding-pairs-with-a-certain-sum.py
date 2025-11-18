class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        # initialize map for nums2 that is a count of each value
        self.nums2_count = defaultdict(int)
        for num in nums2:
            self.nums2_count[num] += 1

    def add(self, index: int, val: int) -> None:
        # old val is changing so decrement count
        old_val = self.nums2[index]
        self.nums2_count[old_val] -= 1

        # add val and update count
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            target = tot - num
            if target in self.nums2_count:
                res += self.nums2_count[target]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)