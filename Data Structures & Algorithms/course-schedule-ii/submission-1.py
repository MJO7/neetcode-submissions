class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []

        for courses,prereqs in prerequisites:
            prereq[courses].append(prereqs)

        in_line = set()
        finished = set()

        res = []

        def dfs(course):
            if course in in_line:
                return False
            if course in finished:
                return True
            
            in_line.add(course)

            for prereq_course in prereq[course]:
                if not dfs(prereq_course):
                    return False
                

            in_line.remove(course)
            finished.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 
    