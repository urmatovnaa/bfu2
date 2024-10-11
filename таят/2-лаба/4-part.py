""" Автомат L1 """
status = 'q'
str_now = input("Введите строку: ")
str_end = str_now
counter = 0
print(status, str_end)
for i in str_now:
    if status == 'q':
        if i == 'a':
            status = 'p'
        elif i == 'b':
            status = 'r'
        else:
            break
    elif status == 'p':
        if i == 'b':
            status = 'q'
        elif i != 'a':
            break
    elif status == 'r':
        if i == 'a':
            status = 'q'
        elif i != 'b':
            break
    counter += 1
    str_end = str_now[counter::]
    print(status, str_end)

if not str_end and status == 'r':
    print("Строка прошла автомат")
else:
    print("Строка не прошла автомат")