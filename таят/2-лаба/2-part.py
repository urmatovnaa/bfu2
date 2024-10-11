status = '0'
str_now = input("Введите строку: ")
str_end = str_now
counter = 0
print(status, str_end)
for i in str_now:
    if status == '0' and i == 'b':
        status = '01'
    elif status == '01':
        if i == 'a':
            status = '1'
        elif i != 'b':
            break
    else:
        if i != 'a':
            break
    counter += 1
    str_end = str_now[counter::]
    print(status, str_end)

if not str_end:
    print("Строка прошла автомат")
else:
    print("Строка не прошла автомат")