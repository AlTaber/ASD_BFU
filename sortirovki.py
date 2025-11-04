import time
import random

def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения сортировки '{function.__name__}': {end - start:.9f} s")
        return result
    return wrapper

@measure_time
def comb_sort(arr):        # №4 Сортировка методом прочёсывания
    n = len(arr)
    step = n
    flag = False
    while step > 1 or flag:
       if step > 1:
           step = int(step / 1.25)
       flag, i = False, 0
       while i + step < n:
          if arr[i] > arr[i + step]:
              arr[i], arr[i + step] = arr[i + step], arr[i]
              flag = True
          i += step
    return arr

@measure_time
def insertion_sort(arr):   # №5 Сортировка вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@measure_time
def selection_sort(arr):   # №6 Сортировка выбором
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                arr[k], arr[min_index] = arr[min_index], arr[k]
    return arr

@measure_time
def shell_sort(arr):       # №7 Сортировка Шелла
    pass

@measure_time
def radix_sort(arr):       # №8 Поразрядная сортировка
    pass

@measure_time
def heap_sort(arr):        # №9 Пирамидальная (heap sort)
    pass

@measure_time
def merge_sort(arr):       # №10 Сортировка слиянием
    pass

@measure_time
def quick_sort(arr):       # №11 Быстрая сортировка
    pass

@measure_time
def external_sort(filename):  # №12 Внешняя многофазная сортировка
    pass

if __name__ == "__main__":

    A = list(range(1, 51))
    B = A[::-1]
    C = A.copy()
    random.shuffle(C)

    for arr in [A, B, C]:
        print("⏺️  Применение сортировок для массива:")
        print(arr)
        print("---------------------------------------------")
        for sort_function in [comb_sort, insertion_sort, selection_sort, ]: #shell_sort, radix_sort, heap_sort, merge_sort, quick_sort, sort]:
            a = arr.copy()
            print('Успешно ✅' if sort_function(a) == A else 'Ошибка ❌')
        print("---------------------------------------------")
        
