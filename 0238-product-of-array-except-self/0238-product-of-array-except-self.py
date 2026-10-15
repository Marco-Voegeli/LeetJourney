class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first prefix
        prefix = [1]
        for num in nums[:-1]:
            prefix.append(num*prefix[-1])
        # then suffix
        suffix = [1]
        for num in nums[::-1]:
            suffix.append(num*suffix[-1])
        suffix.reverse()
        return [a*b for (a,b) in zip(prefix, suffix[1:])]