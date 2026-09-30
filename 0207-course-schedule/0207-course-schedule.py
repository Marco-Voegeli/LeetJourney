from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # DFS down, counting the nodes seen
        # We need to count the number of incoming and outgoing edges
        # We need a queue to add the children in
        # We need a set to put the visited nodes in
        visited = [False] * numCourses
        path = [False] * numCourses
        edge_map = {}
        for [i, j] in prerequisites:
            if j in edge_map:
                edge_map[j].append(i)
            else:
                edge_map[j] = [i]


        def dfs(course):
            if visited[course] or course not in edge_map:
                return True
            visited[course] = path[course] = True
            
            for next_course in edge_map[course]:
                if path[next_course]:
                    return False
                if not dfs(next_course):
                    return False
            path[course] = False
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

