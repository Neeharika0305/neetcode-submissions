class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}

        for num in nums:
            count += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1

        return count