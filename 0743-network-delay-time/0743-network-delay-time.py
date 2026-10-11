class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        times_dict = {}

        for (u, v, w) in times:
            if u in times_dict:
                times_dict[u].append((w, v))
            else:
                times_dict[u] = [(w, v)]
        
        heap = []
        nodes_times = {k: 0}
        
        if k in times_dict:
            for child in times_dict[k]:
                heappush(heap, child)
        while heap:
            (child_time, child_node)= heappop(heap)
            if child_node in nodes_times:
                nodes_times[child_node] = min(child_time, nodes_times[child_node])
            else:
                nodes_times[child_node] = child_time
                if child_node in times_dict:
                    for sub_child in times_dict[child_node]:
                        heappush(heap, (sub_child[0] + child_time, sub_child[1]))
        print(nodes_times)
        return max(nodes_times.values()) if len(nodes_times) == n  else -1 

        


            

        


