from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):

            # Remove index outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Start recording when window size becomes k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result