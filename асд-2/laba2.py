import math

def intersection_lines(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y

def intersection_line_segment(a, b, c, x1, y1, x2, y2):
    p = intersection_lines(a, b, c, y2 - y1, x1 - x2, x1 * y2 - x2 * y1)
    if p and min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2):
        return p
    return None

def intersection_segments(x1, y1, x2, y2, x3, y3, x4, y4):
    p = intersection_lines(y2 - y1, x1 - x2, x1 * y2 - x2 * y1, y4 - y3, x3 - x4, x3 * y4 - x4 * y3)
    if p and min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2) \
         and min(x3, x4) <= p[0] <= max(x3, x4) and min(y3, y4) <= p[1] <= max(y3, y4):
        return p
    return None

def intersection_line_circle(a, b, c, cx, cy, r):
    d = abs(a * cx + b * cy + c) / math.sqrt(a**2 + b**2)
    if d > r:
        return None
    elif d == r:
        x = cx - a * c / (a**2 + b**2)
        y = cy - b * c / (a**2 + b**2)
        return [(x, y)]
    else:
        x0, y0 = cx - a * c / (a**2 + b**2), cy - b * c / (a**2 + b**2)
        h = math.sqrt(r**2 - d**2)
        dx, dy = -b * h / math.sqrt(a**2 + b**2), a * h / math.sqrt(a**2 + b**2)
        return [(x0 + dx, y0 + dy), (x0 - dx, y0 - dy)]

def intersection_segment_circle(x1, y1, x2, y2, cx, cy, r):
    points = intersection_line_circle(y2 - y1, x1 - x2, x1 * y2 - x2 * y1, cx, cy, r)
    return [p for p in points if min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2)]

def intersection_circles(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return None
    elif d == 0 and r1 == r2:
        return []       #"Бесконечное количество точек"
    elif d == r1 + r2 or d == abs(r1 - r2):
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        x_t = x1 + a * (x2 - x1) / d
        y_t = y1 + a * (y2 - y1) / d
        return [(x_t, y_t)]
    else:
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)
        xm = x1 + a * (x2 - x1) / d
        ym = y1 + a * (y2 - y1) / d
        xh, yh = h * (y2 - y1) / d, h * (x2 - x1) / d
        return [(xm + xh, ym - yh), (xm - xh, ym + yh)]

def vector_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def area(A, B, C):
    return abs((A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2.0)

def is_point_inside_triangle(P, A, B, C):
    S_ABC = area(A, B, C)
    S_PAB = area(P, A, B)
    S_PBC = area(P, B, C)
    S_PCA = area(P, C, A)
    if not S_ABC or  not S_PCA or  not S_PAB or not S_PBC:
        return False
    return abs(S_PAB + S_PBC + S_PCA - S_ABC) < 1e-9  # Проверяем с учетом погрешности

def is_triangle_inside(T1, T2):
    A, B, C = T1
    D, E, F = T2

    return (is_point_inside_triangle(A, D, E, F) and
            is_point_inside_triangle(B, D, E, F) and
            is_point_inside_triangle(C, D, E, F))

def find_triangles(points):
    triangles = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
             for k in range(j + 1, n):
                  if vector_product(points[i], points[j], points[k]):
                      triangles.append((points[i], points[j], points[k]))
    return triangles

def find_nested_triangles(points):
    triangles = find_triangles(points)

    for T1 in triangles:
        for T2 in triangles:
            if T1 != T2 and is_triangle_inside(T1, T2):
                print(T1, T2)
                return True

    return False

points = [(0, 0), (9, 0), (4, 5), (1, 1), (2, 2), (3, 3)]
points2 = [(0, 0), (5, 0), (7, 0), (5, 6), (7, 2)]
find_nested_triangles(points2)
