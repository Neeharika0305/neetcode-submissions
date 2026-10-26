class Solution:
    def longestConsecutive(self, nums):

        # Create our own hash table
        table = {}

        for num in nums:
            table[num] = True

        longest = 0

        for num in nums:

            # Duplicate check:
            # only start if num - 1 doesn't exist
            if (num - 1) not in table:

                length = 1
                current = num

                while (current + 1) in table:
                    current += 1
                    length += 1

                if length > longest:
                    longest = length

        return longest