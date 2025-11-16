PRIORITY = 0
USER = 1

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}  # taskId: Node
        self.pq = []

        # initialize data structures
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = [priority, userId]
        heappush(self.pq, [-priority, -taskId]) # max heap


    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks[taskId][PRIORITY] = newPriority
        heappush(self.pq, [-newPriority, -taskId])
        # keep old entry and ignore later by checking if priority equals entry in map


    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]


    def execTop(self) -> int:
        while self.pq:
            priority, taskId = heappop(self.pq)
            priority, taskId = -priority, -taskId

            # stale value
            if taskId not in self.tasks or priority != self.tasks[taskId][PRIORITY]:
                continue

            userId = self.tasks[taskId][USER]
            del self.tasks[taskId]
            return userId

        return -1


"""
Things that need to be efficient:
- getting the top priority task (for execution)
    - multiple tasks can have same priority
- accessing a given task
- removing a given task
- adding a task
    - must add into data structures efficiently
    - be in proper position based on priority

data structures:
- hashmap of task id to node
    - efficient for accessing, removing, and adding a specific task
- priority queue tasks (ordered by priority break ties by task id)
    - efficient for getting top priority
    - once given node, efficient for accessing, removing, and adding a specific task

task:
- user
- task
- priority
"""


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()