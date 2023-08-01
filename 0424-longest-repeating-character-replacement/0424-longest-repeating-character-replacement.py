class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            most_common_count = max(charCount.values())
            if (r - l + 1) - most_common_count <= k:
                longest = max(longest, r - l + 1)
            else:
                charCount[s[l]] -= 1
                l += 1
        return longest

"""
SLIDING WINDOW TECHNIQUE

~ iterate through string while keeping left pointer
~ keep making window bigger while condition is true
~ condition is if there are a valid amount of switches such that the substring would be the same character
~ to check condition, keep track of the amount of times the most common character in the current substring occurs. Then do length of current substring minus that number. If result is <= k, then condition is true
~ after checking condition each time, set longest to be max(longest, len(substring))

~ to check amount of times the most common character in the substring occurs
~ use map to count character occurrences and return max value

~ when condition is not met, slide window over by incrementing the left pointer until condition is satisfied again
~ also decrement the char count value at the previous left pointer index
"""