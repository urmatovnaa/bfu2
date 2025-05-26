#Задача о самом большом подмассиве: поиск непрерывного подмассива в одномерном массиве чисел с наибольшей суммой.
#Алгоритм Кадане

def max_submassive(nums):
    if not nums:
        return 0

    curr_sum = max_sum = nums[0]
    start = end = start_i = 0;

    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
            start_i = i
        else:
            curr_sum += nums[i]
        if max_sum <= curr_sum:
            max_sum = curr_sum
            end = i
            start = start_i

    print(nums[start:end + 1])
    return max_sum


nums = [2, -1, 3, 4, -1, -2, 1, -5, 4]
print(max_submassive(nums))
