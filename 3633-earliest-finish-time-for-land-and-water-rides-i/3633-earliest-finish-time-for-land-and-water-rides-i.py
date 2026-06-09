class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        '''
        endTimes = []
        for st, d in zip(landStartTime, landDuration):
            landEndTime = st + d
            for wSt,wD in zip(waterStartTime, waterDuration):
                finalEndTime = max(landEndTime, wSt) + wD        
                endTimes.append(finalEndTime)
        for st, d in zip(waterStartTime, waterDuration):
            waterEndTime = st + d
            for lSt,lD in zip(landStartTime, landDuration):
                finalEndTime = max(waterEndTime, lSt) + lD        
                endTimes.append(finalEndTime)
        return min(endTimes)
        '''
        landEndTime = min(st+d for st,d in zip(landStartTime, landDuration))
        waterEndTime = min(st+d for st,d in zip(waterStartTime, waterDuration))

        ans = 9999999
        for st,d in zip(waterStartTime, waterDuration):
            ans = min(ans, max(landEndTime, st) + d)
        for st,d in zip(landStartTime, landDuration):
            ans = min(ans, max(waterEndTime, st) + d)
        return ans