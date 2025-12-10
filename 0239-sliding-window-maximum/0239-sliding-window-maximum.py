class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = defaultdict(int)
        l, r = 0, 0
        while r < k:
            heappush(heap, -nums[r])
            counts[nums[r]] += 1
            r += 1

        res = [-heap[0]]
        while r < len(nums):
            # update l then increment
            counts[nums[l]] -= 1
            if -heap[0] == nums[l]:
                heappop(heap)
            l += 1

            #update r then increment
            counts[nums[r]] += 1
            heappush(heap, -nums[r])
            r += 1

            # check if top is in counts
            while heap and counts[-heap[0]] == 0:
                heappop(heap)

            res.append(-heap[0])

        return res

"""
for each window, track the max num in that window

brute force:
- for each window, go through each element and find the max
Time: O(n^2)

better:
- initialize a max heap and map of nums in the window
- map is count of nums in window
- for each step, update the map and the heap
- updating the map
    - decrement value on the left
    - increment value on the right
- updating the heap
    - if the value on the left is the top of the heap, pop
    - add the value on the right
- check the max by checking the top of the heap and ensuring it's in the map
    - if not keep popping until the top is in the window
Time: O(n log n)
"""