def selection_sort(arr):
    # Длина массива
    n = len(arr)
    # Внешний цикл: проходит по каждому элементу массива, ставить минимальный элемент на позицию i
    for i in range(n):
        min_index = i # текущий элемент - min
        
        # Внутренний цикл: ищет минимальный элемент в неотсортированной части
        for j in range(i + 1, n):
            # Если найден элемент меньше текущего минимального
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)