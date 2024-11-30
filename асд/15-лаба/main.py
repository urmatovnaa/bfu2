# Рекурсивные обходы (прямой, центральный, концевой)

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
    while index < len(string) and (string[index].isdigit() or (string[index]=='-' and not value) or string[index] == '.'):
        value += string[index]
        index += 1

    if not value:
        raise ValueError("Некорректное значение")

    el = Element(float(value))

    if index < len(string) and string[index] == '(':
        index += 1

        if string[index] != ',':
            el.left, index = build_tree(string, index)

        index += 1

        if string[index] != ')':
            el.right, index = build_tree(string, index)
        index += 1

    return el, index

# Прямой
def preorder(el):
    if el:
        print(el.value, end="  ")
        preorder(el.left)
        preorder(el.right)

# Центральный
def inorder(el):
    if el:
        inorder(el.left)
        print(el.value, end="  ")
        inorder(el.right)

# Концевой
def postorder(el):
    if el:
        postorder(el.left)
        postorder(el.right)
        print(el.value, end="  ")


example = "8 (3 (1.1, 6 (4,7.56)), -10 (, 14(13,)))"

root = prepare_string(example)

preorder(root)
print()
inorder(root)
print()
postorder(root)
