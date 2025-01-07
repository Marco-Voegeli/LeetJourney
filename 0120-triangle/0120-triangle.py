class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle.reverse()
        sums = triangle[0]
        for row in triangle[1:]:
            sums = [a + min(sums[j], sums[j+1]) for (j,a) in enumerate(row)]
        return min(sums)

        