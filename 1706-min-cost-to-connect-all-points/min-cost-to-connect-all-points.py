class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:      
        n = len(points)
        used = [False] * n  # уже добавленные точки
        cost = [10**9] * n  # минимальная стоимость 
        
        cost[0] = 0  # старт
        result = 0  # итог        
        for _ in range(n):
            u = -1
            
            # ближайшая точка
            for i in range(n):
                if not used[i] and (u == -1 or cost[i] < cost[u]):
                    u = i
            
            used[u] = True # добавляем в MST
            result += cost[u] # прибавляем стоимость
            
            # обновляем расстояния 
            for v in range(n):
                if not used[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    cost[v] = min(cost[v], d)
        
        return result