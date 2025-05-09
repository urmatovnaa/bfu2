def floyd_warshall(matrix):
    n = len(matrix)
    next_node = [[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != float('inf'):
                next_node[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    next_node[i][j] = next_node[i][k]

    return matrix, next_node

def reconstruct_path(i, j, next_node):
    if next_node[i][j] is None:
        return [i, j] if i != j else [i]
    path = [i]
    while i != j:
        i = next_node[i][j]
        path.append(i)
    return path

def tsp(sub_matrix, cities):
    n = len(sub_matrix)
    VISITED_ALL = (1 << n) - 1
    INF = 10**18
    dp = [[(INF, []) for _ in range(n)] for _ in range(1 << n)]

    for i in range(n):
        dp[1 << i][i] = (0, [cities[i]])

    for mask in range(1 << n):
        for i in range(n):
            current_cost, current_path = dp[mask][i]
            if current_cost == INF:
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue

                new_mask = mask | (1 << j)
                new_cost = current_cost + sub_matrix[i][j]
                new_path = current_path + [cities[j]]

                if new_cost < dp[new_mask][j][0]:
                    dp[new_mask][j] = (new_cost, new_path)

    return min(dp[VISITED_ALL][i] for i in range(n))

def build_submatrix(matrix, cities):
    n = len(cities)
    sub = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub[i][j] = matrix[cities[i]][cities[j]]
    return sub

def shortest_road(matrix, cities_to_visit):
    matrix, next_node = floyd_warshall(matrix)
    sub_matrix = build_submatrix(matrix, cities_to_visit)
    cost, path = tsp(sub_matrix, cities_to_visit)

    full_path = [path[0]]
    for i in range(len(path)-1):
        segment = reconstruct_path(path[i], path[i+1], next_node)
        full_path += segment[1:]

    return cost, full_path

dist = [
    [0, 29, 2, 46, 68, 52, 72, 42, 11, 55],
    [29, 0, 55, 34, 42, 46, 50, 29, 20, 58],
    [2, 55, 0, 68, 46, 42, 43, 91, 38, 50],
    [46, 34, 68, 0, 82, 15, 72, 54, 33, 48],
    [68, 42, 46, 82, 0, 29, 12, 52, 37, 32],
    [52, 46, 42, 15, 29, 0, 45, 50, 10, 72],
    [72, 50, 43, 72, 12, 45, 0, 38, 20, 65],
    [42, 29, 91, 54, 52, 50, 38, 0, 41, 29],
    [11, 20, 38, 33, 37, 10, 20, 41, 0, 50],
    [55, 58, 50, 48, 32, 72, 65, 29, 50, 0]
]

cities_to_visit = [2, 4, 6, 8]
shortest_road(dist, cities_to_visit)
