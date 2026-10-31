class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            ss = " ".join(sorted(i))
            if ss in d:
                d[ss].append(i)
            else:
                d[ss] = [i]
        return list(d.values())

        