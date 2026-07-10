class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DAG and then we do DFS on it and add a node once we explored all of its children a
        dag = {i: [] for i in range(numCourses)} # nodes and the neighbors
        res = []
        for (a,b) in prerequisites:
            dag[b].append(a)
        visited = [0 for i in range(numCourses)] # 0 unvisited; 1 in process; 2 fully processed
        def dfs(node_i):
            visited[node_i] = 1
            for neighbor in dag[node_i]:
                if visited[neighbor] == 1:
                    return 
                elif visited[neighbor] == 0:
                    dfs(neighbor)
            visited[node_i] = 2
            res.append(node_i)
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        for visit in visited:
            if visit == 1:
                return [] # cycle detected
        res.reverse()
        return res
