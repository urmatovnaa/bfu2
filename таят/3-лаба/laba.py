import random

def generate_nfh_grammar():
    # Нормальная форма Хомского
    def S():
        choice = random.randrange(1, 3)
        if choice == 1: return K() + G()
        return L() + A()

    def A():
        choice = random.randrange(1, 3)
        if choice == 1: return H() + G()
        return ""

    def B():
        return "("

    def C():
        return "]"

    def D():
        return B() + B()

    def F():
        return  A() + C()

    def G():
        return C() + A()

    def H():
        return B() + A()

    def K():
        return D() + F()

    def L():
        return H() + C()
    return S()


def generate_nfg_grammar():
    # Нормальная форма Грейбаха
    def A0():
        choice = random.randrange(1, 3)
        if choice == 1: return "(" + A1() + A3() + A1()
        return "(" + A2() + A4() + A5()

    def A1():
        choice = random.randrange(1, 3)
        if choice == 1: return "(" + A1() + A5()
        return ""

    def A2():
        return "("

    def A3():
        return "]"

    def A4():
        return "(" + A1() + A5() + A3()

    def A5():
        return ']' + A1()

    return A0()

# Генерация строк
print("Строка из Нормальной формы Хомского:")
for _ in range(5):
    print(generate_nfh_grammar())

print("\nСтрока из Нормальной формы Грейбаха:")
for _ in range(5):
    print(generate_nfg_grammar())

