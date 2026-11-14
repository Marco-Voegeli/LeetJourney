from collections import deque
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i+1 : set() for i in range(n)}
        for time in times:
            u, v, w = time[0], time[1], time[2]
            graph[u].add((w, v))

        queue = list(graph[k])  
        heapq.heapify(queue)
        visited = set([k])
        res = float(inf)
        while queue:
            (w, v) = heapq.heappop(queue)
            if v in visited:
                continue
            visited.add(v)
            if len(visited) == n:
                res = min(res , w)
            for edge in graph[v]:
                if edge[1] in visited:
                    continue
                heapq.heappush(queue, (w + edge[0], edge[1]))
        return res if res < float(inf) else -1
            
             