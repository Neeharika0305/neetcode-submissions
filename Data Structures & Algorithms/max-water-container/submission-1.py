class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0

        while i < j:
            w = j - i
            h = min(heights[i],heights[j])
            s = w * h
            if s > max_area:
                max_area = s

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area