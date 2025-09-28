class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, -1 * abs(stone1 - stone2))

        return -1 * stones[0] if stones else 0