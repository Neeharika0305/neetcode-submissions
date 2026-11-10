class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Character has required frequency
            if char in need and window[char] == need[char]:
                have += 1

            # Window is valid
            while have == need_count:
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_start = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]