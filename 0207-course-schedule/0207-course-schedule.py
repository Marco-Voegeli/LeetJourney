from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the DAG; if you can make it to the end you are good.
        incoming_count = {i:0 for i in range(numCourses)}
        out_to_in = {i: [] for i in range(numCourses)}
        queue = deque()
        counter = 0
        for (a, b) in prerequisites:
            incoming_count[a] += 1
            out_to_in[b].append(a)
        for a in incoming_count:
            if incoming_count[a] == 0:
                counter += 1
                queue.append(a)
        while queue:
            for neighbor in out_to_in[queue.pop()]: # is this pop only happening once or on every loop?
                incoming_count[neighbor] -= 1
                if incoming_count[neighbor] == 0:
                    counter += 1
                    queue.append(neighbor)    

        return True if counter == numCourses else False

        