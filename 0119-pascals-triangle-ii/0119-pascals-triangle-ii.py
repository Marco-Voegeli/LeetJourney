class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = [1,1]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return prev_row
        for i in range(1, rowIndex):
            curr_row = [1]

            for j in range(i):
                curr_row.append(prev_row[j] + prev_row[j+1])
            curr_row.append(1)
            prev_row = curr_row
        return prev_row        