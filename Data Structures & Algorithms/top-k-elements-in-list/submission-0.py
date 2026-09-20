class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:

                d[i] = 1
        
        a = []
        for i in d:
            a.append([d[i],i])

        a.sort(reverse=True)

        r = []
        for i in range(k):
            r.append(a[i][1])
        return r
        