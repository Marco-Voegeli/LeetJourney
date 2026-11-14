from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {i: set() for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        res = 0
        pool = set([i for i in range(n)])
        while pool:
            val = pool.pop()
            pool.add(val)
            res += 1
            queue = deque([val])
            while queue:
                val = queue.popleft()
                if val not in pool:
                    continue
                pool.remove(val)
                for city in graph[val]:
                    if city in pool:
                        queue.append(city)
        return res