class Solution:
    def numOfSubsequences(self, s: str) -> int:
        # calculate # of subsequences and prefix counts
        count_l, count_lc, count_lct = 0, 0, 0
        prefix_l, prefix_lc = [0] * (len(s) + 1), [0] * (len(s) + 1)
        for i, c in enumerate(s):
            prefix_l[i + 1] = prefix_l[i]
            prefix_lc[i + 1] = prefix_lc[i]

            if c == 'L':
                count_l += 1
                prefix_l[i + 1] += 1
            elif c == 'C':
                count_lc += count_l
                prefix_lc[i + 1] += count_l
            elif c == 'T':
                count_lct += count_lc
            
        
        # suffix counts
        suffix_t, suffix_ct = [0] * (len(s) + 1), [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            suffix_t[i] = suffix_t[i + 1]
            suffix_ct[i] = suffix_ct[i + 1]

            c = s[i]
            if c == 'T':
                suffix_t[i] += 1
            elif c == 'C':
                suffix_ct[i] += suffix_t[i]
        
        # see best after inserting
        # prefix[0] is 0
        # suffix[len(s)] is 0
        extra = 0
        for i in range(len(s)):
            # inserting L
            extra = max(extra, suffix_ct[i])

            # inserting C
            extra = max(extra, prefix_l[i + 1] * suffix_t[i])

            # inserting T
            extra = max(extra, prefix_lc[i + 1])
        
        return count_lct + extra

"""
- to count the number of subsequences we can do the following
- have a count_l, count_lc, and count_lct
    - each count value is the number of subsequences (ways to form that string)
for c in s:
    if c == 'L': count_l += 1
    if c == 'C': count_lc += count_l
    if c == 'T': count_lct += count_lc

- have prefix counts and suffix counts for each index (counts are # subsequences)
- prefix counts for L and LC
- suffix counts for T and CT

- go through each index and see what the best option insertion is
- for L, the extra # of subsequences is the suffix CT count
- for C, the extra # of subequences is prefix L * suffix T
- for T, the extra # of subsequences is the prefix LC count
"""

"""
went down the wrong path below
- preprocess by getting indices of L, C, and T
    - lists will be in order

- count number of subsequences algorithm:
for each idx_l in indices of L:
    for each idx_c in indices of C:
        if idx_c < idx_l:
            continue

        for each idx_t in indices of T:
            if idx_t < idx_c:
                continue
            
            count += 1

- brute force be trying to add one of the letters before and after each index
    - try adding an L before and after each index present in all indices of L, C, and T
    - same thing with C, and then same thing with T
    - will take a long time

- best answer will be adding the letter that contributes the least to the num
    - can figure out which letter contributes the least by the following
        - have a set for each L, C, and T
        - everytime a subsequence is found, add the indices to the sets
        - set with smallest length is letter that contributes the least
    - if L or T contribute the least then it's simply just adding the letters to the ends
        - multiplies # of subsequences by 2

LLLCCCTTT
"""