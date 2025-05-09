import sys

def vector_product(o, a, b):
    #векторное произведение для определения ориентации поворота
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    """Алгоритм Грэхема для нахождения выпуклой оболочки"""
    points = sorted(set(points))

    if len(points) < 3:
        return None

    lower = []
    for p in points:
        while len(lower) >= 2 and vector_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and vector_product(upper[-2], upper[-1], p) <= 0:   # поворот правый или лежит на одной прямой
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

n = int(input("Введите количество точек: "))
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Поиск выпуклой оболочки
hull = convex_hull(points)

if len(hull) > 2:
    print("Выпуклая оболочка существует. Её вершины:")
    for p in hull:
        print(p)
else:
    print("Выпуклая оболочка не существует.")
