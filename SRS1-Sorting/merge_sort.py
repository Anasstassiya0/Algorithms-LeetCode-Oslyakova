def merge_sort(arr):
    # Если в массиве один элемент или меньше - он уже считается отсортированным
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    # Делим массив на две части
    left = arr[:mid]
    right = arr[mid:]
  
    # Рекурсивно сортируем левую и правую часть
    left = merge_sort(left)
    right = merge_sort(right)

    # Объединяем два отсортированных массива
    return merge(left, right)


def merge(left, right):
    result = []  # результирующий массив
    i = 0
    j = 0
    # Сравниваем элементы двух массивов
    while i < len(left) and j < len(right):
        # Добавляем меньший элемент в результат
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [38, 27, 43, 3, 9, 82, 10]
print("Отсортированный массив:", merge_sort(numbers))
