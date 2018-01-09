def bfs_iterative(graph, start):
    visited, queue = [], [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    queue.append(node)
    return visited


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])}

print(bfs_iterative(graph, 'A'))
