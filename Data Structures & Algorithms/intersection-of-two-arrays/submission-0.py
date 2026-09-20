class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = set(nums1)
        d = set()

        for i in nums2:
            if i in c:
                d.add(i)
        return list(d)        