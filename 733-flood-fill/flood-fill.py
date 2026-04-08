class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc] #исходный цвет 

        if start == color:
            return image

        def dfs(r, c):
            # если выходит за границы - остановить
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            # если цвет не совпадает - остановить
            if image[r][c] != start:
                return
            
            # окращеваем текущую клетку
            image[r][c] = color
            dfs(r + 1, c)  # вниз
            dfs(r - 1, c)  # вверх
            dfs(r, c + 1)  # вправо
            dfs(r, c - 1)  # влево

        dfs(sr, sc)
        return image