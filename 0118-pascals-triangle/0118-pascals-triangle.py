class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        pascals = [[1]]
        for i in range(1, numRows):
            new_row = [1]
            for j in range(1,i):
                new_row.append(pascals[i-1][j-1] + pascals[i-1][j])
            new_row.append(1)
            pascals.append(new_row)
        return pascals