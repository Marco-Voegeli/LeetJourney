class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # build all combinations for [1, ..., 9 for k spaces so 9ck] then find their sum; then return list of combinations equal to n.
        curr_n = n
        candidates = []
        
        def recurse(k, start, target, bag):
            if target == 0 and k == 0:
                candidates.append(list(bag))
                return
            if target < 0 or k < 0:
                return 
            else:
                for i in range(start, 10):
                    if i in bag or i > target:
                        continue
                    bag.add(i)
                    recurse(k-1, i, target-i, bag)
                    bag.remove(i)

        recurse(k, 1, n, set())
        return candidates