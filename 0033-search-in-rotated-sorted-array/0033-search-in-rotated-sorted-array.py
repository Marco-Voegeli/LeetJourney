class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search_k(l, r, target):
            k = 0
            while r >= l:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    k = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return k

        def binary_search_target(l, r, k, target):
            i = 0
            reset_l = 0
            reset_r = len(nums) - 1 
            while reset_l <= reset_r:
                mid = reset_l + (reset_r - reset_l) // 2
                if target == nums[(mid + k) % len(nums)]:
                    return (mid + k) % len(nums)
                elif target < nums[(mid + k) % len(nums)]:
                    reset_r = mid - 1
                else:
                    reset_l = mid + 1
            return -1
        # finding k
        k = binary_search_k(0, len(nums)-1, nums[0])
        
        return binary_search_target(k, (len(nums) + k - 1)% len(nums), k, target)
