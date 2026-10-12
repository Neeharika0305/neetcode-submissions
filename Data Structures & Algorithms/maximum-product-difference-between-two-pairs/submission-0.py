
class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()

        max_product = nums[-1] * nums[-2]
        min_product = nums[0] * nums[1]

        return max_product - min_product