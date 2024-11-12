import random

def generate_nfh_grammar():
    # Нормальная форма Хомского
    def S():
    	random
        return K() + A() + G()

    def A():
        if random.random() < 0.5:
            return A() + A()
        else:
            return ""

    return S()

def generate_nfg_grammar():
    # Нормальная форма Грейбаха
    def S():
        return "(" + A() + "]"

    def A():
        if random.random() < 0.5:
            return S()
        else:
            return ""

    return S()

# Генерация строк
print("Строка из Нормальной формы Хомского:")
for _ in range(5):
    print(generate_nfh_grammar())

print("\nСтрока из Нормальной формы Грейбаха:")
for _ in range(5):
    print(generate_nfg_grammar())

