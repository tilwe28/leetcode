class AllOne:

    def __init__(self):
        self.counts = {"": 0}
        self.min_key = ""
        self.max_key = ""

    def inc(self, key: str) -> None:
        # check if exists
        if key in self.counts:
            self.counts[key] += 1

            # check if previous min and recompute
            if key == self.min_key:
                curr_min = self.counts[key]
                for k, c in self.counts.items():
                    if k == "":
                        continue
                    if c < curr_min:
                        curr_min = c
                        self.min_key = k
        
        # doesn't exist, so add and set as min
        else:
            self.counts[key] = 1
            self.min_key = key

        # check if key is now max
        if self.counts[key] > self.counts[self.max_key]:
            self.max_key = key

    def dec(self, key: str) -> None:
        self.counts[key] -= 1

        # check if previous max and recompute
        if key == self.max_key:
            curr_max = self.counts[key]
            for k, c in self.counts.items():
                if k == key:
                    continue
                if c >= curr_max:
                    curr_max = c
                    self.max_key = k

        # delete if 0
        if self.counts[key] == 0:
            # if key was previously min then set to something else
            if key == self.min_key:
                self.min_key = self.max_key  # in case nothing else exists
                curr_min = self.counts[self.max_key]
                for k, c in self.counts.items():
                    if k == "" or k == key:
                        continue
                    if c < curr_min:
                        curr_min = c
                        self.min_key = k
            
            # delete
            del self.counts[key]
            return

        # check if key is now min
        if self.counts[key] < self.counts[self.min_key]:
            self.min_key = key

    def getMaxKey(self) -> str:
        return self.max_key

    def getMinKey(self) -> str:
        return self.min_key

"""
- map of key string to count
- min is the latest one inserted
- if value is incremented and was the previous min
    - re check min
- if vlaue is decremented and was the previous max
    - re check max
"""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()