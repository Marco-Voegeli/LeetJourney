class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for intv in intervals:
            if not res:
                res.append(intv)
            res_elem = res[-1] # Has the smallest start interval
            if res_elem[1] >= intv[0]:
                res[-1] = [res_elem[0], max(res_elem[1], intv[1])]
            if res_elem[1] < intv[0]: 
                res.append(intv)
        return res


            