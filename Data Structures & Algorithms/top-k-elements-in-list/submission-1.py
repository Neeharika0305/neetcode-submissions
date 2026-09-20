class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequency
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into their frequency bucket
        for i in d:
            frequency = d[i]
            buckets[frequency].append(i)

        # Step 4: Collect from highest frequency
        result = []

        for frequency in range(len(buckets) - 1, 0, -1):

            for i in buckets[frequency]:

                result.append(i)

                if len(result) == k:
                    return result