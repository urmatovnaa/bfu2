def table_transition(pattern, alphabet):
    """
    Таблица переходов для конечного автомата
    """
    m = len(pattern)
    transition = {}

    for q in range(m + 1):
        for a in alphabet:
            k = q + 1
            while k > 0 and pattern[:k] != (pattern[:q] + a)[-k:]:
                k -= 1
            transition[(q, a)] = k

    return transition


def automaton_search(text, pattern):
    """
    Конечный автомат для поиска всех вхождений образца в тексте.
    """
    alphabet = set(text)
    transition = table_transition(pattern, alphabet)

    m = len(pattern)
    n = len(text)
    q = 0
    matches = []

    for i in range(n):
        q = transition.get((q, text[i]), 0)
        if q == m:
            matches.append(i - m + 1)

    return matches


# Пример использования
text = "fabcabc"
pattern = "abc"
print("Позиции вхождений:", automaton_search(text, pattern))
