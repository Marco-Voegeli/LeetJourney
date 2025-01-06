class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx_1 = 1
        idx_2 = 1
        min_num = math.pow(-10, 9)
        for idx_res in range(1, m + n + 1):
            if n - idx_2 >= 0: 
                tail2 = nums2[-idx_2]
            else: tail2 = min_num
            if m - idx_1 >= 0:
                tail1 = nums1[m - idx_1]        
            else: tail1 = min_num
            if tail1 > tail2:
                nums1[-idx_res] = tail1
                idx_1 += 1
            else:
                nums1[-idx_res] = tail2
                idx_2 += 1
        return None