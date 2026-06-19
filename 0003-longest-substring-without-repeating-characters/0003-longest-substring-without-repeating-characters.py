class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_window = ""
        res = ""
        for c in s:
            if c not in sliding_window:
                sliding_window = sliding_window + c
            else:
                res = sliding_window if len(sliding_window) > len(res) else res
                sliding_window = sliding_window.split(c, 1)[1] + c
        return max(len(sliding_window),len(res))