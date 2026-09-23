class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        max_len = 0
        for c in s:
            if c in window:
                max_len = max(max_len, len(window))
                window = window.split(c)[1]
            window += c
        return max(max_len, len(window))