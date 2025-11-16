import time
import random

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

def insertion_sort(arr):   # №5 Сортировка вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):   # №6 Сортировка выбором
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                arr[k], arr[min_index] = arr[min_index], arr[k]
    return arr

def shell_sort(arr):       # №7 Сортировка Шелла
    last_index = len(arr)
    step = len(arr)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2
    return arr

def radix_sort(arr):       # №8 Поразрядная сортировка
    max_digits = max([len(str(x)) for x in arr])

    base = 10

    bins = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]

        bins = [[] for _ in range(base)]
    return arr

def heap_sort(arr):        # №9 Пирамидальная (heap sort)
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def merge_sort(arr):       # №10 Сортировка слиянием
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged

def quick_sort(arr):       # №11 Быстрая сортировка
    pass

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
        for sort_function in [comb_sort, insertion_sort, selection_sort, shell_sort, radix_sort, heap_sort, merge_sort, ]: #quick_sort]:
            a = arr.copy()
            start = time.time()
            result = sort_function(a)
            end = time.time()
            time_result = end - start
            print(sort_function.__name__ + (': Успешно ✅ ' if result == A else ': Ошибка ❌') + f" {time_result:.9f} s")
        print("---------------------------------------------")
        
