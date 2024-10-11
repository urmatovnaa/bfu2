# 1-часть

status = 'S'
str_now = input("Введите строку: ")
str_end = str_now
counter = 0

for i in str_now:
    str_end = str_now[counter::]
    print(status, str_end)
    if status == 'S':
        if i == 'a':
            status = 'B1'
        elif i == 'b':
            status = 'B2'
        else:
            break
    elif status == 'B1':
        if i == 'c':
            status = 'C1'
        elif i != 'b':
            break
    elif status == 'B2':
        if i == 'a':
            status = 'C2'
        else:
            break
    counter += 1
    if status == 'C1' or status == 'C2' or status == 'C3':
        str_end = str_now[counter::]
        if not str_end:
            status = 'F'
            print(status, str_end)
            break
        elif ('ba' in str_now or 'ab' in str_end) and str_end[0] == 'c':
            break
        elif str_end[0] == 'c':
            status = 'C3'
        else:
            status = 'S'


if not str_end and status == 'F':
    print("Строка прошла автомат")
else:
    print("Строка не прошла автомат")
