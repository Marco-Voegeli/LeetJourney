class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for intv in intervals:
            if not res:
                res.append(intv)
            res_intv = res.pop()
            if res_intv[1] >= intv[0]:
                res.append([res_intv[0], max(intv[1], res_intv[1])])
            else:
                res.append(res_intv)
                res.append(intv)
        return res

            