class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for num in nums:
            if num in viewed:
                return True
            else:
                viewed.add(num)
        return False