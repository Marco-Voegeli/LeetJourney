
class Solution:
    
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Max number of overlaps == Min number of groups
        n = len(intervals)
        events = []

        for i in intervals:
            events.append((i[0], 1))
            events.append((i[1] + 1, -1))
        sorted_events = sorted(events)  
        print(sorted_events)
        max_val = 0
        counter = 0
        for x in sorted_events:
            counter += x[1]
            if counter > max_val:
                max_val = counter
        return max_val