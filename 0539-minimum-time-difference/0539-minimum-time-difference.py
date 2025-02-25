class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        HOURS_IN_DAY = 24
        MINS_IN_HOUR = 60
        MINS_IN_DAY = MINS_IN_HOUR * HOURS_IN_DAY

        times = []
        for time in timePoints:
            h, m = time.split(":")
            mins_passed = (int(h) * 60) + int(m)
            times.append(mins_passed)

        times.sort()
        min_diff = MINS_IN_DAY
        for i in range(len(times) + 1):
            curr_diff = abs(times[i % len(times)] - times[(i - 1) % len(times)])
            if curr_diff > MINS_IN_DAY / 2:
                curr_diff = MINS_IN_DAY - curr_diff

            min_diff = min(min_diff, curr_diff)

        return min_diff

"""
INITIAL THOUGHTS:
- for each time, calculate time away from midnight
    - convert time to amount of minutes passed in the day
    - mins_passed = HH * 60 + MM
- sort list
- track min_dist
    - an extra for the first and last
    - if curr_dist > 720, then curr_dist = 1440 - curr_dist
    - b/c max time difference can only be 12 hours
Time: O(n log n) <- sorting array
Space: O(n)
"""