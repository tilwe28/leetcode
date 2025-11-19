class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end_times = []

        res = 1
        curr_needed = 1
        for start, end in intervals:
            # removing meetings that have finished (start is "curr" time)
            while end_times and start >= end_times[0]:
                heappop(end_times)
                curr_needed -= 1

                # always need at least 1
                if curr_needed == 0:
                    curr_needed = 1
            
            # check if meetings still happening
            if end_times and start < end_times[0]:
                curr_needed += 1

            heappush(end_times, end)
            res = max(res, curr_needed)

        return res
            

"""
essentially trying to count maximum number of overlapping intervals at once

initial thoughts:
- sort intervals by start time
- have a priority queue (min heap) of end times
- iterate through intervals
- have curr overlapping count (track max)
    - if overlapping, add 1
    - if start is after min end, sub 1
        - do this part in a loop

- condition for overlap:
    - curr_start < prev_end

-----
-------
 --------
        --------
"""