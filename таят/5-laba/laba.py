# Логические операторы и их приоритеты
OPERATORS = {
    '->': (1, 'right'),       # Импликация
    '<->': (1, 'right'),      # Эквиваленция
    'v': (2, 'left'),         # OR
    '^': (3, 'left'),         # AND
    '!': (4, 'right')         # NOT
}

# Функция для преобразования выражения в обратную польскую нотацию
def infix_to_rpn(expression):
    output = []
    operators = []
    
    # Функция для обработки оператора
    def process_operator(op):
        while operators and operators[-1] != '(':
            top = operators[-1]
            if (OPERATORS[op][1] == 'left' and OPERATORS[op][0] <= OPERATORS[top][0]) or \
               (OPERATORS[op][1] == 'right' and OPERATORS[op][0] < OPERATORS[top][0]):
                output.append(operators.pop())
            else:
                break
        operators.append(op)

    tokens = tokenize(expression)
    
    for token in tokens:
        if token.isdigit():  # Если токен - операнд (логическая константа)
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError("Синтаксическая ошибка: несбалансированные скобки")
            operators.pop()  # Убираем '(' из стека
        elif token in OPERATORS:
            process_operator(token)
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    
    while operators:
        op = operators.pop()
        if op in ('(', ')'):
            raise ValueError("Синтаксическая ошибка: несбалансированные скобки")
        output.append(op)
    
    return output

# Функция для вычисления выражения в обратной польской нотации
def evaluate_rpn(rpn_tokens):
    stack = []
    
    for token in rpn_tokens:
        if token.isdigit():  # Если токен - логическая константа
            stack.append(int(token))
        elif token in OPERATORS:
            if token == '!':  # Унарный оператор (NOT)
                operand = stack.pop()
                stack.append(int(not operand))
            else:  # Бинарные операторы
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if token == '->':  # Импликация
                    stack.append(int(not operand1 or operand2))
                elif token == '<->':  # Эквиваленция
                    stack.append(int(operand1 == operand2))
                elif token == 'v':  # OR
                    stack.append(int(operand1 or operand2))
                elif token == '^':  # AND
                    stack.append(int(operand1 and operand2))
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    
    if len(stack) != 1:
        raise ValueError("Синтаксическая ошибка в выражении")
    
    return stack[0]

# Функция для токенизации выражения (разделение на операнды и операторы)
def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        if expression[i].isdigit():  # Операнд
            tokens.append(expression[i])
        elif expression[i] in '()':
            tokens.append(expression[i])
        elif expression[i] == '!':
            tokens.append(expression[i])
        elif expression[i:i+2] == '->':
            tokens.append('->')
            i += 1
        elif expression[i:i+3] == '<->':
            tokens.append('<->')
            i += 2
        elif expression[i] == 'v':
            tokens.append('v')
        elif expression[i] == '^':
            tokens.append('^')
        else:
            raise ValueError(f"Неизвестный символ: {expression[i]}")
        i += 1
    return tokens

# Главная функция
def main(expression):
    try:
        rpn = infix_to_rpn(expression)
        print("Обратная польская нотация:", " ".join(rpn))
        result = evaluate_rpn(rpn)
        print("Результат:", result)
    except ValueError as e:
        print("Ошибка:", e)

# Пример использования
expression = "(1 ^ 0) -> 1"
main(expression)

