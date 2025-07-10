from collections import defaultdict

class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, string):
        self.chart = [set() for _ in range(len(string) + 1)]
        self.chart[0].add(("S", 0, 0))  # Добавляем стартовое состояние

        for i in range(len(string) + 1):
            added = True
            while added:
                added = False
                for state in list(self.chart[i]):
                    if self._is_complete(state):
                        added |= self._complete(state, i)
                    elif self._is_nonterminal(state):
                        added |= self._predict(state, i)
                    else:
                        added |= self._scan(state, i, string)

        # Таблица разбора
        self._print_chart(string)

        # Проверка, принадлежит ли строка грамматике
        for state in self.chart[-1]:
            if state[0] == "S" and state[1] == len(self.grammar["S"][0]) and state[2] == 0:
                return True
        return False

    def _is_complete(self, state):
        # Проверяем, завершён ли анализ правила
        head, pos, _ = state
        rule = self.grammar.get(head, [[]])[0]
        return pos == len(rule)

    def _is_nonterminal(self, state):
        # Проверяем, является ли текущий символ нетерминалом
        head, pos, _ = state
        rule = self.grammar.get(head, [[]])[0]
        return pos < len(rule) and rule[pos].isupper()

    def _predict(self, state, index):
        # Добавляем состояния для новых правил, порождаемых текущим нетерминалом
        head, pos, _ = state
        rule = self.grammar.get(head, [[]])[0]
        next_symbol = rule[pos]
        added = False
        for production in self.grammar.get(next_symbol, []):
            new_state = (next_symbol, 0, index)
            if new_state not in self.chart[index]:
                self.chart[index].add(new_state)
                added = True

            if production == ["e"]:  # Если пустое правило
                completed_state = (head, pos + 1, state[2])
                if completed_state not in self.chart[index]:
                    self.chart[index].add(completed_state)
                    added = True
        return added

    def _scan(self, state, index, string):
        # Сканируем текущий символ строки
        head, pos, start = state
        rule = self.grammar.get(head, [[]])[0]
        if index < len(string) and pos < len(rule) and rule[pos] == string[index]:
            new_state = (head, pos + 1, start)
            if new_state not in self.chart[index + 1]:
                self.chart[index + 1].add(new_state)
                return True
        return False

    def _complete(self, state, index):
        # Завершаем обработку правила
        head, pos, start = state
        added = False
        for prev_state in self.chart[start]:
            prev_head, prev_pos, prev_start = prev_state
            prev_rule = self.grammar.get(prev_head, [[]])[0]
            if prev_pos < len(prev_rule) and prev_rule[prev_pos] == head:
                new_state = (prev_head, prev_pos + 1, prev_start)
                if new_state not in self.chart[index]:
                    self.chart[index].add(new_state)
                    added = True
        return added

    def _print_chart(self, string):
        print("Таблица разбора:")
        for i, states in enumerate(self.chart):
            print(f"Позиция {i}: {string[:i]} -> {string[i:]}")
            for state in states:
                head, pos, start = state
                rule = self.grammar.get(head, [[]])[0]
                print(f"  {head} -> {''.join(rule[:pos])}·{''.join(rule[pos:])}, {start}")
            print()

if __name__ == "__main__":
    # Пример грамматики
    grammar = {
        "S'": [["S"]],
        "S": [["+", "a", "b", "b", "A", "c", "c"]],
        "A": [["b", "A", "c"], ["e"]]
    }

    # Пример строки для разбора
    string = "+abbbccc"

    parser = EarleyParser(grammar)
    if parser.parse(string):
        print(f"Строка '{string}' входит в грамматику.")
    else:
        print(f"Строка '{string}' НЕ входит в грамматику.")
