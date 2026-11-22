
class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        result = [0] * n

        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):
            left_count = i
            right_count = n - i - 1

            left_diff = nums[i] * left_count - left_sum

            right_sum = total_sum - left_sum - nums[i]
            right_diff = right_sum - nums[i] * right_count

            result[i] = left_diff + right_diff

            left_sum += nums[i]

        return result
