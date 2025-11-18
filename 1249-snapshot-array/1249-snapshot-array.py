class SnapshotArray:

    def __init__(self, length: int):
        self.array = [{0: 0} for _ in range(length)]
        self.curr_snap = 0

    def set(self, index: int, val: int) -> None:
        self.array[index][self.curr_snap] = val

    def snap(self) -> int:
        self.curr_snap += 1
        return self.curr_snap - 1
 
    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.array[index]:
            # get older value (not necessarily snap_id - 1)
            older_sid = 0
            for sid, value in self.array[index].items():
                if sid > snap_id:
                    continue
                older_sid = max(older_sid, sid)
            return self.array[index][older_sid]
        return self.array[index][snap_id]
        
"""
initial thoughts:
- brute force solution with really bad memory
- have a map of snap_ids to array

other approach:
- list of maps, where each map is snap_id: value
"""

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)