# На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /".
# Также есть скобочки. Окончанием выражения служит "=".
# Программа должна вывести результат выражения
# Пример ввода:
# 2+7*(3/9)-5=

def calculator(operators, numbers):
    num1 = numbers.pop()
    num2 = numbers.pop()
    operator = operators.pop()

    if operator == '+':
        numbers.append(num2 + num1)
    elif operator == '-':
        numbers.append(num2 - num1)
    elif operator == '*':
        numbers.append(num2 * num1)
    elif operator == '/':
        if num1 == 0:
            print("Нельзя делить на ноль!")
            return False
        numbers.append(num2 / num1)
    return True


equation = input("Введите задачу:")

operators = []  # Будем хранить операторы
numbers = []  # Будем хранить числы
i = 0   # итератор
priority = {'*':1, '/':1, '-':2, '+':2, ')':3, '(':3}  # словарь с приоритетами
correct = True
brackets = 0

while True:
    if i == len(equation):
        break
    if equation[i].isdigit():
        num = ''
        while i < len(equation) and equation[i] not in '()+-/*=':
            num += equation[i]
            i += 1
        numbers.append(float(num))
        continue
    elif equation[i] == '(':
        brackets += 1
        operators.append(equation[i])
    elif equation[i] == ')':
        if not brackets:
            print("Скобки не правильные")
            correct = False
            break
        while operators and operators[-1] != '(':
            if not calculator(operators, numbers):
                correct = False
        operators.pop()
        brackets -= 1
    elif equation[i] in '+-*/':
        while True:
            if operators and operators[-1] != '(' and priority.get(operators[-1]) <= priority.get(equation[i]):
                if not calculator(operators, numbers):
                    correct = False
            else:
                break
        operators.append(equation[i])
    elif equation[i] == '=':
        break
    if not correct:
        break
    i += 1

while operators and correct:
    if len(numbers) < 2:
        print("Скобки не правильные")
        correct = False
        break
    if not calculator(operators, numbers):
        correct = False
        break
if correct:
    print(numbers[0])




    
