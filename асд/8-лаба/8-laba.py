# Сортировка поразрядная
# d * (n + 10)
# d - кол разрядов в самом большом числе
# 20 - 90

def get_digit(number, d_place):
    return (number // 10 ** (d_place - 1)) % 10

def counting_sort(massive, d_place):
    length = len(massive)
    result = [0] * length
    count = [0] * 10

    for number in massive:
        digit = get_digit(number, d_place)
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(length - 1, -1, -1):
        digit = get_digit(massive[i], d_place)
        result[count[digit] - 1] = massive[i]
        count[digit] -= 1

    for i in range(length):
        massive[i] = result[i]


def main_sort(massive):
    maximum = massive[0]
    for num in massive:
        if maximum < num:
            maximum = num

    for i in range(len(str(maximum))):
        counting_sort(massive, i + 1)

list1 = [53, 21, 41, 5, 6, 38, 77, 0, 90, 6, 27, 789, 59, 2, 57, 29, 67, 14, 70]
main_sort(list1)

print(list1)