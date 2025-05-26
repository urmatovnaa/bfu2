# n + m

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    return lps

# print(compute_lps("AABAAAAB"))
#[0, 1, 0, 1, 2, 2, 2, 3]

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    print(lps)
    j = 0
    result = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            result.append(i - m + 1)
            j = lps[j - 1]

    return result

example_text = "Девочка писала стихи: про цветы, принцесс и принцев, про зиму со снегирями и кислый лимон, про ложку, которая прыгает в стакане, когда идет поезд коркоркорк"

kmp_search(example_text, "коркорк")
