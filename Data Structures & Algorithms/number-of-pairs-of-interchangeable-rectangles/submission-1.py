class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        pairs = 0

        for w, h in rectangles:
            ratio = w / h

            if ratio in count:
                pairs += count[ratio]

            count[ratio] = count.get(ratio, 0) + 1

        return pairs