import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = {}
        for task in tasks:
            if task in tasks_dict:
                tasks_dict[task] += 1
            else:
                tasks_dict[task] = 1
        tasks_heap = [(value, key) for (key,value) in tasks_dict.items()]
        heapq.heapify_max(tasks_heap)
        
        res= []
        cooldown_q = deque([])
        time = 0
        idle = 'idle'
        while tasks_heap or cooldown_q:
            if cooldown_q:
                (release_time, task_count, released_task) = cooldown_q[0]
                if release_time < time:
                    cooldown_q.popleft()
                    heapq.heappush_max(tasks_heap, (task_count, released_task))
            if tasks_heap:
                task_count, task = heapq.heappop_max(tasks_heap)
                res.append(task)
                if task_count > 1:
                    cooldown_q.append((time+n, task_count-1, task))
            else:
                res.append(idle)
            time += 1
        return len(res)





            # Keep adding elems not in range
            # Need to hold the subwindow

