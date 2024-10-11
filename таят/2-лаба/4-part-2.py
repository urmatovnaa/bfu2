""" Автомат L2 """
status = 'p'
str_now = input("Введите строку: ")
str_end = str_now
counter = 0
print(status, str_end)
for i in str_now:
    if status == 'q':
        if i == 'a':
            status = 'r'
        elif i != 'b':
            break
    elif status == 'p':
        if i == 'b':
            status = 'q'
        elif i != 'a':
            break
    elif status == 'r':
        if i == 'b':
            status = 'p'
        elif i != 'a':
            break
    counter += 1
    str_end = str_now[counter::]
    print(status, str_end)

if not str_end and status == 'q':
    print("Строка прошла автомат")
else:
    print("Строка не прошла автомат")