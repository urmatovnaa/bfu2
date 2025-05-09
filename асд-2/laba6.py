#Реализовать алгоритм Рабина-Карпа для поиска по образцу

def hash(s):
    m = len(s)
    return sum(ord(s[i]) * (10 ** (m - 1 - i)) for i in range(m))

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)

    p_hash = hash(pattern)
    result = []

    for i in range(n - m + 1):
        word = text[i:i + m]
        s_hash = hash(word)

        if s_hash == p_hash:
            correct = True
            for j in range(m):
                if pattern[j] != word[j]:
                    correct = False
            if correct:
                result.append(i)

    return result

rabin_karp("ABABCABAB", "ABAB")
