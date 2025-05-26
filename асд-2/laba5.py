# Реализовать алгоритм Бойера-Мура для поиска по образцу

def bad_character_table(pattern):
    """таблица плохого символа"""
    bad_char = {}
    m = len(pattern)
    for i in range(m - 1):
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)

    bad_char = bad_character_table(pattern)
    print(bad_char)
    result = []

    shift = 0
    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            print(text[shift+j])
            print(pattern[j], "paaa")
            j -= 1

        if j < 0:
            result.append(shift)
            if shift + m < n:
                next_char = text[shift + m]
                shift += m - bad_char.get(next_char, -1)
                print(shift, "final")
            else:
                shift += 1
        else:
            mismatch_char = text[shift + j]
            shift += max(1, j - bad_char.get(mismatch_char, -1))
            print(shift)

    return result

boyer_moore("AAABABBA", "ABA")
