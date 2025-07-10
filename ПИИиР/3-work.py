def check_number(str_number, digits_count=4, can_repeat=False):
    if len(str_number) != digits_count:
        return False
    if not str_number.isdigit():
        return False
    if len(set(str_number)) != digits_count and not can_repeat:
        return False
    return True


def get_picked_number():
    while True:
        print('Загадайте число')
        str_number = input()
        if check_number(str_number):
            return str_number
            break

        print('Вы ввели неверное число')


def get_guess_number():
    while True:
        print('Введите число')
        str_number = input()
        if check_number(str_number):
            return str_number
            break

        print('Вы ввели неверное число')


def count_cows(picked_number, guess_number):
    count = 0

    for i in guess_number:
        if i in picked_number:
            count += 1
    return count


def count_bulls(picked_number, guess_number):
    count = 0

    for n in range(len(picked_number)):
        if picked_number[n] == guess_number[n]:
            count += 1

    return count


def main():
    tries_count = 0

    picked_number = get_picked_number()

    while True:
        guess_number = get_guess_number()
        tries_count += 1

        if picked_number == guess_number:
            print('Ты выиграл!!!')
            print('Число попыток: ', tries_count)
            return

        cows_count = count_cows(picked_number, guess_number)
        bulls_count = count_bulls(picked_number, guess_number)

        print(f'Найдено {cows_count} коров и {bulls_count} быков')


main()