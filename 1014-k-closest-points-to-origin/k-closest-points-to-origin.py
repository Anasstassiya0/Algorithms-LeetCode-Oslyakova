import heapq

class Solution:
    def kClosest(self, points, k):
        
        heap = []
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            distance = x * x + y * y
            
            heapq.heappush(heap, (-distance, points[i]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result