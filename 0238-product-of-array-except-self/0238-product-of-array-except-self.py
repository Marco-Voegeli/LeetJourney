class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # How to build a prefix - at i we need product of all values before i
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[i]*nums[i])

        # How to build a suffix - at i we need product of all values after i
        # So basically flipped
        suffix = (len(nums) + 1) * [1]
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]

        prefix = prefix[:-1]
        suffix = suffix[1:]
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        return nums