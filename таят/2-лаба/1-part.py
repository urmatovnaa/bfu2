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
            status = 'A'
        elif i == 'b':
            status = 'F'
        else:
            break
    elif status == 'A':
        if i == 'a':
            status = 'B'
        elif i == 'b':
            status = 'C'
        else:
            break
    elif status == 'B':
        if i == 'c':
            status = 'A'
        elif i == 'b':
            status = 'B'
        else:
            break
    elif status == 'C':
        if i == 'a':
            status = 'F'
        elif i == 'b':
            status = 'A'
        else:
            break
    counter += 1
    if status == 'F':
        str_end = str_now[counter::]
        print(status, str_end)
        break

if not str_end and status == 'F':
    print("Строка прошла автомат")
else:
    print("Строка не прошла автомат")
