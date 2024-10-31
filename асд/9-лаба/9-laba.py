# сортировка пирамидальная nlogn-всегда

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

def heap_sort(arr):
    n = len(arr)

    # Строим кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем по одному элементы и перемещяем в конец
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


list1 = [53, 21, 41, 5, 6, 38, 70, 0, 90, 6, 27, 789, 59, 2, 57, 29, 67, -5, 14, 70]
heap_sort(list1)
print(list1)