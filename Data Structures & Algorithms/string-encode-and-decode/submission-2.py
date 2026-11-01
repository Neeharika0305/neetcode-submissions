class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            j = i

            # Find #
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Get actual string
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            # Move i to next encoded string
            i = j + 1 + length

        return result