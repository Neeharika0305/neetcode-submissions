
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0

        while i < len(word) and j < len(abbr):

            # If current character is a digit
            if abbr[j].isdigit():

                # Leading zero is invalid
                if abbr[j] == '0':
                    return False

                num = 0

                # Calculate the complete number
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                # Skip characters in word
                i += num

            else:

                # Compare characters
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
