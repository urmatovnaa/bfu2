# быстрая сортировка nlogn, n

def quicksort(massive):
    if len(massive) <= 1:
        return massive

    pivot = massive[len(massive) // 2]
    left, middle, right = [], [], []
    for x in massive:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort(left) + middle + quicksort(right)


list1 = [53, 21, 41, 5, 6, 38, 70, 0, 90, 6, 27, 789, 59, 2, 57, 29, 67, -5, 14, 70]
sorted_list = quicksort(list1)
print(sorted_list)