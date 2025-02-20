class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        print(sorted_intervals)
        result = []
        result.append(sorted_intervals[0])
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            if interval[0] <= result[-1][1]:
                # merge
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result

"""
BRUTE FORCE:
- sort list on start time
- traverse intervals
    - if start_i < end_i-1, then merge intervals
    - have initial start and end
"""