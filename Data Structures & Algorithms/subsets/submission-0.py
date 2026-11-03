
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []
        current = []

        def backtrack(index):

            # Every current subset is a valid answer
            result.append(current.copy())

            # Try including each remaining element
            for i in range(index, len(nums)):

                current.append(nums[i])

                backtrack(i + 1)

                # Remove the last element (backtracking)
                current.pop()

        backtrack(0)

        return result
