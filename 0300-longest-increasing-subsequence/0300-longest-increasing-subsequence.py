class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memoiz = {nums[0]: 1} # max_elem : length
        for num in nums[1:]:
            lengths = [v for (k,v) in memoiz.items() if k < num]
            if lengths:
                memoiz[num] = max(lengths) + 1
            else:
                memoiz[num] = 1
        print("memoiz: ", memoiz)
        return max([v for v in memoiz.values()]) 

            
                
                