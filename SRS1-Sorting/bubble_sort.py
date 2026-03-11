def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл отвечает за количество проходов по массиву
    # Наибольший элемент перемещается в конец массива 
    for i in range(n):
        swapped = False
        # Внутренний цикл проходит по неотсортированной части массива
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Если порядок неправильный - меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # массив уже отсортирован
        if not swapped:
            breakив
    return arr
  
numbers = [5, 1, 4, 2, 8]
print("Отсортированный массив:", bubble_sort(numbers))
