class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []

        for courses,prereqs in prerequisites:
            prereq[courses].append(prereqs)

        in_line = set()
        finished = set()

        def dfs(course):
            if course in in_line:
                return False
            if course in finished:
                return True

            in_line.add(course)

            for required_course in prereq[course]:
                if not dfs(required_course):
                    return False

            in_line.remove(course)
            finished.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        