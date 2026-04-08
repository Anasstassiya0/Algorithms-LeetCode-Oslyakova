class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []         
        fresh_count = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))  # гнилые
                elif grid[row][col] == 1:
                    fresh_count += 1  # свежие

        minutes_passed = 0

        # BFS
        while queue and fresh_count > 0:
            next_queue = []  # новые гнилые

            for row, col in queue:
                for d_row, d_col in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row = row + d_row
                    new_col = col + d_col

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        next_queue.append((new_row, new_col))

            queue = next_queue  # переходим к следующей очереди
            minutes_passed += 1

        return minutes_passed if fresh_count == 0 else -1