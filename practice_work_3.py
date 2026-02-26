# %%
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
# %%
import random
def partition(arr, low, high):  # разделение Lomuto
    pivot = arr[high] # опорный элемент
    i = low - 1 # индекс меньших элементов
    for j in range(low, high):
        if arr[j] <= pivot: # если текущий элемент меньше или равен pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # меняем местами
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = random.randint(low, high) #случайный pivot
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot_pos = partition(arr, low, high)
        if pivot_pos == k:
            return arr[pivot_pos]
        elif k < pivot_pos: # ищем в левой части
            return quickselect(arr, low, pivot_pos - 1, k)
        else: # ищем в правой части
            return quickselect(arr, pivot_pos + 1, high, k)
num = [9, 3, 7, 1, 8, 2, 5]
k = 3
result = quickselect(num, 0, len(num) - 1, k)
print("Массив:", num)
print(f"{k+1}-й самый маленький элемент:", result)