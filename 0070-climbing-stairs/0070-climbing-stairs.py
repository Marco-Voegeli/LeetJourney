class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairsRec(n: int, prev_values: dict):
            if n == 1:
                return 1
            if n == 2:
                return 2 
            if n in prev_values:
                return prev_values[n]
            n_ways_one = 0
            n_ways_two = 0
            if n-1 > 0:
                n_ways_one = climbStairsRec(n-1, prev_values)
            if n-2 > 0:
                n_ways_two = climbStairsRec(n-2, prev_values)
            prev_values[n] = n_ways_one + n_ways_two
            return prev_values[n]
        prev_val = {}
        return climbStairsRec(n, prev_val)