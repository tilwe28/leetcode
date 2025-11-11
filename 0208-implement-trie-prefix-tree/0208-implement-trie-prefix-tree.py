class Node:
    def __init__(self, letter: str, end=False):
        self.letter = letter
        self.end = end
        self.next = {}

class Trie:

    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node(c)
            curr = curr.next[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)