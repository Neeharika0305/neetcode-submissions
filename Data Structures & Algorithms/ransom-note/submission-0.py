class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = {}

        for i in magazine:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        for j in ransomNote:
            if j not in s or s[j] == 0:
                return False
            s[j] -= 1
        return True
        