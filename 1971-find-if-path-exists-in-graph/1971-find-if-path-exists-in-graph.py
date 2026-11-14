from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {i:set() for i in range(n)}
        
        for (u,v) in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        queue = deque([source])
        visited = set()

        while queue:
            u = queue.popleft()
            if u in visited:
                continue
            if u == destination:
                return True
            visited.add(u)
            for v in graph[u]:
                queue.append(v)
        return False

        
            