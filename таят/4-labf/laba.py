class CYKParser:
    def __init__(self, grammar):
        self.grammar = self._convert_grammar(grammar)

    def _convert_grammar(self, grammar):
        # Преобразуем грамматику в удобный формат для CYK
        cnf = {}
        for head, productions in grammar.items():
            for production in productions:
                prod = tuple(production)
                if prod not in cnf:
                    cnf[prod] = []
                cnf[prod].append(head)
        return cnf

    def parse(self, string):
        n = len(string)
        table = [[set() for _ in range(n)] for _ in range(n)]

        # Заполняем первую строку таблицы
        for i, symbol in enumerate(string):
            for head in self.grammar.get((symbol,), []):
                table[i][i].add(head)

        # Заполняем таблицу для остальных строк
        for length in range(2, n + 1):  # Длина текущей подстроки
            for start in range(n - length + 1):  # Начало подстроки
                for split in range(1, length):  # Точка разделения
                    left_cell = table[start][start + split - 1]
                    right_cell = table[start + split][start + length - 1]

                    for A in left_cell:
                        for B in right_cell:
                            for head in self.grammar.get((A, B), []):
                                table[start][start + length - 1].add(head)

        # Вывод таблицы
        self._print_table(table, string)

        # Проверяем, принадлежит ли строка грамматике
        return 'S' in table[0][n - 1]

    def _print_table(self, table, string):
        print("Таблица CYK:")
        n = len(string)
        for i in range(n):
            for j in range(i, n):
                print(f"  ({i}, {j}): {table[i][j]}")
            print()

if __name__ == "__main__":
    # Пример грамматики в CNF (исправленный)
    grammar = {
        'S': [['LM']],
        'A': [['HC'], ['e']],
        'B': [['b']],
        'C': [['c']],
        'D': [['+']],
        'F': [['a']],
        'G': [['DF']],
        'H': [['BA']],
        'K': [['CC']],
        'L': [['GB']],
        'M': [['HK']]
    }

    # Пример строки для разбора
    string = "+abbbccc"

    parser = CYKParser(grammar)
    if parser.parse(string):
        print(f"Строка '{string}' входит в грамматику.")
    else:
        print(f"Строка '{string}' НЕ входит в грамматику.")
