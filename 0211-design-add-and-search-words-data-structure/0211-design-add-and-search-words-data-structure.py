class Node:
    def __init__(self):
        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node()
            curr = curr.next[c]
        curr.end = True

    def backtrack(self, word: str, node: Node) -> bool:
        if not word:
            return node.end
        
        curr = node
        for i, c in enumerate(word):
            if c == '.':
                # backtrack
                for l in curr.next.keys():
                    if self.backtrack(word[i+1:], curr.next[l]):
                        return True
                return False
            elif c not in curr.next:
                return False
            
            curr = curr.next[c]
        
        return curr.end

    def search(self, word: str) -> bool:
        return self.backtrack(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)