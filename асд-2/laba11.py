#Решить задачу о раскраске графа.

def graph_coloring(vertices, edges):
    coloring = dict()

    for vertex in vertices:
        used_colors = set()
        for edge in edges:
            if vertex in edge:
                neighbor = edge[0] if edge[1] == vertex else edge[1]
                if neighbor in coloring:
                    used_colors.add(coloring[neighbor])

        for color in range(1, len(vertices) + 1):
            if color not in used_colors:
                coloring[vertex] = color
                break

    return {
        "Количество использованных цветов": max(coloring.values()),
        "Раскраска графа": coloring
    }

vertices = [1, 2, 3, 4]
edges = [(4, 1), (1, 2), (2, 3), (3, 4)]
graph_coloring(vertices, edges)
