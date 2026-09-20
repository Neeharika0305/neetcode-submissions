class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxi = 0
        t = set()

        for j in range(len(s)):
            while s[j] in t:
                t.remove(s[i])
                i += 1
            t.add(s[j])
            maxi = max(maxi,j-i+1)
        return maxi
        