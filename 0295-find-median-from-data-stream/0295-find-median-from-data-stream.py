class MedianFinder:

    def __init__(self):
        self.left = []  # max heap (store values as negatives)
        self.right = []  # min heap (larger by 1 for odd number of values)
        
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        # add initial values to each half
        if not self.right:
            heapq.heappush(self.right, num)
            return
        if not self.left:
            heapq.heappush(self.left, -1 * heapq.heappushpop(self.right, num))
            return

        # add num to correct half
        if num < -1 * self.left[0]:
            heapq.heappush(self.left, -1 * num)
        else:
            heapq.heappush(self.right, num)

        # rebalance
        if len(self.left) > len(self.right):
            # multiply by -1 to revert back to normal value
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            # multiply by -1 to store as max heap
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return ((-1 * self.left[0]) + self.right[0]) / 2
        return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()