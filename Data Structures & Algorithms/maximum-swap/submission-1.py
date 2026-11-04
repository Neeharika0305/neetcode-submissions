
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        max_index = len(digits) - 1
        left = -1
        right = -1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[max_index]:
                max_index = i
            elif digits[i] < digits[max_index]:
                left = i
                right = max_index

        if left != -1:
            digits[left], digits[right] = digits[right], digits[left]

        return int("".join(digits))
