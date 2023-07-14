class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            groups[tuple(letters)].append(s)
        return groups.values()