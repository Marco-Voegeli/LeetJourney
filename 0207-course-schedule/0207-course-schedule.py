from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       

        # how to build a graph
        # we need pair (src, dst)
        in_to_out = { i: [] for i in range(numCourses)}
        incoming_occurences = [0 for i in range(numCourses)]

        counter = 0
        queue = deque()
        # Fill the graph
        for (i, j) in prerequisites:
            if j in in_to_out:
                in_to_out[j].append(i)
            else:
                in_to_out[j] = [i]
            incoming_occurences[i] += 1
        for i in range(len(incoming_occurences)):
            if incoming_occurences[i] == 0:
                counter += 1
                queue.append(i)
        while queue:
            for out in in_to_out[queue.pop()]:
                incoming_occurences[out] -= 1
                if incoming_occurences[out] == 0:
                    counter += 1
                    queue.append(out)
        return True if counter == numCourses else False

