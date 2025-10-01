class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        res = []
        registered, path = set(), set()

        def dfs(course):
            if course in registered:
                return True
            if course in path:
                return False
            
            path.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            registered.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

"""
Map of course to prerequisites
run dfs on map
track courses taken
track path taken to get to course during dfs (avoid cycles)
"""