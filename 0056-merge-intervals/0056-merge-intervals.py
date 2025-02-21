class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        time_map = [0] * (1 + max(interval[0] for interval in intervals))
        for start, end in intervals:
            # can contain duplicate start times
            time_map[start] = max(end + 1, time_map[start])

        res = []
        curr_start = -1
        curr_end = -1
        for i in range(len(time_map)):
            if time_map[i] != 0:
                # actually at interval entry
                if curr_start == -1:
                    curr_start = i

                # time_map[i] - 1 to account for previous + 1
                curr_end = max(curr_end, time_map[i] - 1) 

            if curr_end == i:
                # add interval and reset curr interval
                res.append([curr_start, curr_end])
                curr_start = -1
                curr_end = -1
        
        # add last interval
        if curr_start != -1:
            res.append([curr_start, curr_end])

        return res

"""
BRUTE FORCE:
- sort list on start time
- traverse intervals
    - if start_i < end_i-1, then merge intervals
    - have initial start and end
Time: O(n log n)
Space: O(n)

GREEDY:
- mapping array w/ length 1 + max start time
- map start time to 1 + end time
- store 1 + end time b/c at end time, if 0, we know interval done
- traverse mapping array
    - track current end time
    - if at end time and val is 0, interval is done
    - update along the way as necessary
        - curr_end = max(curr_end, end)
n = num intervals, m = max start time
Time: O(max(n, m))
Space: O(m)
"""