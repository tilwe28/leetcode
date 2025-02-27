class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_prereqs = [[] for _ in range(numCourses)] # adj list
        for course, prereq in prerequisites:
            course_prereqs[course].append(prereq)

        order = []
        registered, path = set(), set()

        def dfs(course) -> bool:
            if course in registered:
                return True
            if course in path:
                # cycle
                return False

            path.add(course)
            for prereq in course_prereqs[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            registered.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

"""
BRUTE FORCE:
- for each course, find it's prereq
- if a course doesn't have a prereq, that can be taken first
- before adding course, check if prereq has been added to taken

edge cases:
- cycles in prereqs

OPTIMAL:
- make prereq map (list of lists)
- DFS for each course
- track path during DFS (used for cycle detection)
- track courses added
- add course at end of DFS traversal / no prereqs unsatisfied
"""