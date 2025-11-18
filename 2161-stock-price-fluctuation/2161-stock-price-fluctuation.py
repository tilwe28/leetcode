class StockPrice:

    def __init__(self):
        self.curr_time = 0
        self.prices = {}
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.curr_time = max(self.curr_time, timestamp)
        self.prices[timestamp] = price
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.curr_time]

    def maximum(self) -> int:
        while True:
            max_price, timestamp = self.max_heap[0]
            max_price = -max_price
            if self.prices[timestamp] != max_price:
                # price was updated
                heappop(self.max_heap)
            else:
                return max_price

    def minimum(self) -> int:
        while True:
            min_price, timestamp = self.min_heap[0]
            if self.prices[timestamp] != min_price:
                # price was updated
                heappop(self.min_heap)
            else:
                return min_price

"""
initial thought:
- updating min and max by iterating through all timestamps
    - iteration only when previous max or min is updated

better:
- use a min heap and max heap
"""


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()