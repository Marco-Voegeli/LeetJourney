class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key= lambda x: x[0])
        res = [intervals[0]]
        for intv in intervals:
            if intv[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intv[1])]
            else:
                res.append(intv)
        return res

        
            
