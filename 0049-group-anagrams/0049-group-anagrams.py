class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            letters = tuple(letters)
            if anagrams.get(letters):
                anagrams[letters].append(s)
            else:
                anagrams[letters] = [s]
        return list(anagrams.values())

"""
Initial Thoughts:
- loop through list of strs
- have some type of mapping for anagram representation and list of strs that satisfy it
- for each str in strs, check if str's anagram representation exists in mapping
    - if so, add str to list
    - else, create new mapping with str in the list

- key for mapping will be tuple of size 26 where the ith index is frequency of that character
"""