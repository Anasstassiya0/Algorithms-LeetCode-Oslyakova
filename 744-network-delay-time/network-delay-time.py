class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        # расстояния 
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0  # стартовая вершина
        
        visited = set()
        
        while len(visited) < n:
            # вершина с минимальным расстоянием
            cur = -1
            cur_dist = float('inf')
            
            for node in range(1, n + 1):
                if node not in visited and dist[node] < cur_dist:
                    cur = node
                    cur_dist = dist[node]
            
            # если не нашли - значит недостижимо
            if cur == -1:
                return -1
            
            visited.add(cur)
            
            if cur in graph:
                for nei, w in graph[cur]:
                    if dist[cur] + w < dist[nei]:
                        dist[nei] = dist[cur] + w
    
        return max(dist.values())