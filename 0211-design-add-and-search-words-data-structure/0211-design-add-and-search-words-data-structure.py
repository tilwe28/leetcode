LETTERS = "abcdefghijklmnopqrstuvwxyz"

class Node:
    def __init__(self, letter: str):
        self.letter = letter
        self.next = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node(c)
            curr = curr.next[c]
        curr.end = True

    def backtrack(self, word: str, node: Node) -> bool:
        if not word:
            return node.end
        
        curr = node
        for i, c in enumerate(word):
            if c == '.':
                # backtrack
                for l in LETTERS:
                    if l in curr.next:
                        res = self.backtrack(word[i+1:], curr.next[l])
                        if res:
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