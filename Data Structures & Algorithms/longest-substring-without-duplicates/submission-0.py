class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        maxLen, curLen = 1, 1

        l, r = 0, 1

        while r < len(s):
            if s[r] not in s[l:r]:
                curLen += 1
                r += 1
            else:
                maxLen = max(curLen, maxLen)
                l += 1
                r = l + 1
                curLen = 1

        return max(maxLen, curLen)
        