"""
Операции над БНП: поиск, добавление, удаление”
Дерево вводится в программу в формате линейно-скобочной записи.
Затем появляется меню, в котором доступна операция добавления, удаления и поиска вершины БДП.
После выполнения операции программа должна возвращаться снова в меню.
При выходе их него до завершения программы на экран должно быть выведено БДН любым способом (в виде линейно-скобочной записи).
"""

# Узел
class Element:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Проверка скобок
def check_parentheses(string):
    balance = 0
    for char in string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


def prepare_string(string):
    if not check_parentheses(string):
        raise ValueError("Некорректная строка: скобки не сбалансированы.")

    string = string.replace(" ", "")

    return build_tree(string)[0]

# Строение дерева
def build_tree(string, index=0):
    if index >= len(string):
        return None, index

    value = ""
    while index < len(string) and (string[index].isdigit() or (string[index]=='-' and not value)):
        value += string[index]
        index += 1

    if not value:
        raise ValueError("Некорректное значение")

    el = Element(int(value))

    if index < len(string) and string[index] == '(':
        index += 1

        if string[index] != ',':
            el.left, index = build_tree(string, index)

        index += 1

        if string[index] != ')':
            el.right, index = build_tree(string, index)
        index += 1

    return el, index

# Поиск
def search(el, key):
    if not el:
        return False
    if key == el.value:
        return True
    elif key < el.value:
        return search(el.left, key)
    else:
        return search(el.right, key)

def insert(el, key):
    if not el:
        return Element(key)
    if key < el.value:
        el.left = insert(el.left, key)
    elif key >= el.value:
        el.right = insert(el.right, key)
    return el

def delete(el, key):
    if not el:
        return None

    if key < el.value:
        el.left = delete(el.left, key)
    elif key > el.value:
        el.right = delete(el.right, key)
    else:
        if not el.left:
            return el.right
        elif not el.right:
            return el.left

        min_larger_node = find_min(el.right)
        el.value = min_larger_node.value
        el.right = delete(el.right, min_larger_node.value)
    return el

def find_min(el):
    current = el
    while current.left:
        current = current.left
    return current

def tree_to_string(el):
    if not el:
        return ""
    left = tree_to_string(el.left) if el.left else ""
    right = tree_to_string(el.right) if el.right else ""
    if left or right:
        return f"{el.value} ({left},{right})"
    else:
        return f"{el.value}"

example = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"

def menu():
    data = input("Введите дерево в линейно-скобочной записи: ")
    root = prepare_string(data)

    while True:
        print("\nМеню:")
        print("1. Поиск элемента")
        print("2. Добавление элемента")
        print("3. Удаление элемента")
        print("4. Выход")
        choice = input("Выберите операцию: ")

        if choice == "1":
            key = int(input("Введите значение для поиска: "))
            found = search(root, key)
            print("Элемент найден." if found else "Элемент не найден.")
        elif choice == "2":
            key = int(input("Введите значение для добавления: "))
            tree = insert(root, key)
            print("Элемент добавлен.")
        elif choice == "3":
            key = int(input("Введите значение для удаления: "))
            tree = delete(root, key)
            print("Элемент удален.")
        elif choice == "4":
            print("Итоговое дерево:", tree_to_string(root))
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

menu()
