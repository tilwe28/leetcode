class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        # swap curr and last in list
        last = self.list[-1]
        curr_idx = self.map[val]
        self.list[curr_idx] = last
        self.map[last] = curr_idx
        self.list.pop()

        del self.map[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)
        
"""
thoughts:
- of course need a set/map of the elements
- have map of vals to indexes into a list
    - allows O(1) insertion and removal
- list of values (corresponding to the map)
    - allows us to randomly index into it regardless of the values
- on removal, in list swap current with last
    - then pop
    - current is no longer needed, so move it to last and remove
"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()