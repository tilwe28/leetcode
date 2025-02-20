class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result

"""
BRUTE FORCE:
- sort list on start time
- traverse intervals
    - if start_i < end_i-1, then merge intervals
    - have initial start and end
Time: O(n log n)
Space: O(n)
"""