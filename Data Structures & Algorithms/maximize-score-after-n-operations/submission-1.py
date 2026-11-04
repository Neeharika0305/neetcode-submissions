
from math import gcd
from functools import lru_cache

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def solve(mask):
            if mask == (1 << n) - 1:
                return 0

            operation = bin(mask).count("1") // 2 + 1
            best = 0

            for i in range(n):
                if mask & (1 << i):
                    continue

                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    score = operation * gcd(nums[i], nums[j])
                    new_mask = mask | (1 << i) | (1 << j)

                    best = max(best, score + solve(new_mask))

            return best

        return solve(0)
