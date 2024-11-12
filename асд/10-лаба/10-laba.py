# сортировка слиянием nlogn - всегда

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def merge_sort(massive):
    if len(massive) <= 1:
        return massive

    mid = len(massive) // 2

    left_half = merge_sort(massive[:mid])
    right_half = merge_sort(massive[mid:])

    return merge(left_half, right_half)


list1 = [53, 21, 41, 5, 6, 38, 70, 0, 90, 6, 27, 789, 59, 2, 57, 29, 67, -5, 14, 70]
sorted_arr = merge_sort(list1)
print(sorted_arr)
