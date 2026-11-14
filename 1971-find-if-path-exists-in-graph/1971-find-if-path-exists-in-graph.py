from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        edges_dict = {i:[] for i in range(n)}
        for (s,d) in edges:
            edges_dict[s].append(d)
            edges_dict[d].append(s)
        visited = set()
        queue = deque()
        queue.append(source)
        while queue:
            v = queue.popleft()
            if v in visited:
                continue
            if v == destination:
                return True
            visited.add(v)
            for u in edges_dict[v]:
                queue.append(u)
        return False
            