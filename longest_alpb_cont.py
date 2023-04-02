class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        if(len(s) < 2):
            return len(s)
        max_sub = 0
        current = 1
        for i in range(1, len(s)):
            if(letters.index(s[i]) - letters.index(s[i-1]) == 1):
                current += 1
            else:
                current = 1
            max_sub = max(max_sub, current)
        return max_sub