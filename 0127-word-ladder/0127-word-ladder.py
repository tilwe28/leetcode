class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        q = deque([beginWord])
        wordSet.discard(beginWord)  # remove if present
        level = 1
        
        while q:
            level_len = len(q)
            for _ in range(level_len):
                word = q.popleft()
                if word == endWord:
                    return level
                
                # generate adjacent words
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            q.append(next_word)
                            wordSet.remove(next_word)  # mark visited
            level += 1
        return 0

"""
thoughts:
- check every combination of changes
- first start trying to change first letter
    - after going down that path, then try starting with changing second letter

- to achieve this, map each word to a list of words that only differ by one
- then do bfs starting with beginWord

- must check words that differ by one
"""