class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c = nums[0]
        m = nums[0]

        for i in range(1,len(nums)):
            c = max(nums[i], c+nums[i])
            m = max(m,c)
        return m        