
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        result = []

        if len(p) > len(s):
            return result

        p_count = [0] * 26
        window_count = [0] * 26

        # Count characters in p and first window
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        # Check first window
        if p_count == window_count:
            result.append(0)

        # Slide the window
        for i in range(len(p), len(s)):

            # Add new character
            window_count[ord(s[i]) - ord('a')] += 1

            # Remove old character
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1

            # Compare frequencies
            if p_count == window_count:
                result.append(i - len(p) + 1)

        return result
