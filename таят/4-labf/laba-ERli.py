class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.start_symbol = next(iter(grammar))  # Начальный символ (первый ключ грамматики)
    
    def parse(self, string):
        n = len(string)
        # Инициализация парсера
        states = [[] for _ in range(n + 1)]
        states[0].append((self.start_symbol, 0, 0))  # Начальное состояние

        # Проход по каждому индексу строки
        for i in range(n + 1):
            for state in states[i]:
                lhs, dot, rule_index = state
                
                # 1. Расширение (Predict)
                if dot < len(self.grammar[lhs]):
                    next_symbol = self.grammar[lhs][dot]
                    if next_symbol in self.grammar:
                        for rule in self.grammar[next_symbol]:
                            states[i].append((next_symbol, 0, len(states[i])))

                # 2. Сканирование (Scan)
                if dot < len(self.grammar[lhs]) and i < n:
                    next_symbol = self.grammar[lhs][dot]
                    if next_symbol == string[i]:
                        states[i + 1].append((lhs, dot + 1, rule_index))

                # 3. Завершение (Complete)
                if dot == len(self.grammar[lhs]):
                    for previous_state in states[rule_index]:
                        prev_lhs, prev_dot, _ = previous_state
                        if prev_dot < len(self.grammar[prev_lhs]) and self.grammar[prev_lhs][prev_dot] == lhs:
                            states[i].append((prev_lhs, prev_dot + 1, rule_index))

        # Проверка завершения
        return any(lhs == self.start_symbol and dot == len(self.grammar[lhs]) for lhs, dot, _ in states[n])


# Пример грамматики
grammar = {
    'S\'': ['+A'],
    'A': ['aD'],
    'D': ['BC'],
    'B': ['bB', 'bc'],
    'C': ['c']
}

# Создание экземпляра парсера
parser = EarleyParser(grammar)

# Пример строки длиной не менее 10
input_string_10 = '+abbcc'
result_10 = parser.parse(input_string_10)
print(f"String '{input_string_10}' parsing result: {result_10}")

# Пример строки длиной не менее 100
input_string_100 = '+abbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
result_100 = parser.parse(input_string_100)
print(f"String '{input_string_100}' parsing result: {result_100}")
