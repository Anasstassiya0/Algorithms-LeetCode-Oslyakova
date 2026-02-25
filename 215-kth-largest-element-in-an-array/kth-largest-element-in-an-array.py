class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        def bubble_up(i):
            while i > 0:
                parent = (i - 1) // 2
                if heap[parent] > heap[i]:
                    heap[parent], heap[i] = heap[i], heap[parent]
                    i = parent
                else:
                    break

        def bubble_down(i):
            n = len(heap)
            while True:
                smallest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right

                if smallest != i:
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
                else:
                    break

        def heappush(val):
            heap.append(val)
            bubble_up(len(heap) - 1)

        def heappop():
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            bubble_down(0)

        for num in nums:
            heappush(num)
            if len(heap) > k:
                heappop()

        return heap[0]