import random
def partition(arr, low, high): #разделения Lamuto
    pivot = arr[high]  #pivot
    i = low - 1        #индекс меньших элементов
    for j in range(low, high): #если текущий элемент меньше или равен pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #меняем местами элементы
    arr[i + 1], arr[high] = arr[high], arr[i + 1] #помещаем pivot между меньшими и большими элементами
    return i + 1
def randomized_quicksort(arr, low, high): #сортируем массив на месте
    if low < high:
        pivot_index = random.randint(low, high) #случайный pivot в конец
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index] #разделяем массив и получаем позицию pivot
        pi = partition(arr, low, high) #рекурсивно сортируем левую часть
        randomized_quicksort(arr, low, pi - 1) #рекурсивно сортируем правую часть
        randomized_quicksort(arr, pi + 1, high)
num = [9, 3, 7, 1, 8, 2, 5]
print("Исходный массив:", num)
randomized_quicksort(num, 0, len(num) - 1)

print("Отсортированный:", num)
