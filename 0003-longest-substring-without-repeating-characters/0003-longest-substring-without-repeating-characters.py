class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_windows = [[]]
        for c in s:
            main_window = sliding_windows[-1]
            if c in main_window:
                sliding_windows.append(main_window[main_window.index(c)+1:] + [c])
            else:
                main_window.append(c)
        len_sliding = [len(window) for window in sliding_windows]
        return max(len_sliding)