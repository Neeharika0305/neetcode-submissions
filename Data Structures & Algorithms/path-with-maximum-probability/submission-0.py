import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int,
                       end: int) -> float:

        graph = [[] for _ in range(n)]

        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        prob = [0.0] * n
        prob[start] = 1.0

        heap = [(-1.0, start)]

        while heap:
            p, node = heapq.heappop(heap)
            p = -p

            if node == end:
                return p

            if p < prob[node]:
                continue

            for nei, edge_prob in graph[node]:
                new_prob = p * edge_prob

                if new_prob > prob[nei]:
                    prob[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0