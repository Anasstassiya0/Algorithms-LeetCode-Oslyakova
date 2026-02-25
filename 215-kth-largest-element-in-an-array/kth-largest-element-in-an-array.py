class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Превращаем список в max-heap через отрицательные значения
        nums = [-num for num in nums]
        
        # Преобразуем список в кучу за O(n)
        heapq.heapify(nums)
        
        # Удаляем k-1 самых больших элементов
        for _ in range(k - 1):
            heapq.heappop(nums)
        
        # Следующий элемент — это k-й наибольший
        return -heapq.heappop(nums)