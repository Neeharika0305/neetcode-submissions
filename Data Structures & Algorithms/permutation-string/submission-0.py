class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        c = {}
        d = {}

        # Build frequency dictionaries
        for i in range(len(s1)):
            if s1[i] not in c:
                c[s1[i]] = 0
            c[s1[i]] += 1

            if s2[i] not in d:
                d[s2[i]] = 0
            d[s2[i]] += 1

        # Check first window
        if c == d:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Add new character
            if s2[right] not in d:
                d[s2[right]] = 0
            d[s2[right]] += 1

            # Remove left character
            d[s2[left]] -= 1

            if d[s2[left]] == 0:
                del d[s2[left]]

            left += 1

            # Compare frequency dictionaries
            if c == d:
                return True

        return False