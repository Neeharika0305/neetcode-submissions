
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        # Step 1: Build the graph
        for i in range(n):
            x1, y1, r = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, _ = bombs[j]

                dx = x1 - x2
                dy = y1 - y2

                if dx * dx + dy * dy <= r * r:
                    graph[i].append(j)

        # Step 2: DFS from every bomb
        def dfs(i, visited):
            visited.add(i)

            for j in graph[i]:
                if j not in visited:
                    dfs(j, visited)

        answer = 0

        for i in range(n):
            visited = set()
            dfs(i, visited)
            answer = max(answer, len(visited))

        return answer
