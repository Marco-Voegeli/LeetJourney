class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        edges_dict = {i:[] for i in range(n)}
        for (s,d) in edges:
            edges_dict[s].append(d)
            edges_dict[d].append(s)
        visited = set()
        def bfs(position):
            if position in visited:
                return False
            if position == destination:
                return True
            visited.add(position)
            res = False
            queue = []
            for v in edges_dict[position]:
                if v == destination:
                    return True
                queue.append(v)
            for v in queue:
                res = res or bfs(v)
            return res
        return bfs(source)
            