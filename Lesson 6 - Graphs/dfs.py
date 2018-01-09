def dfs_iterative(graph, start):
    visited, stack = [], [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    stack.append(node)
    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = []
    elif start in visited:
        return

    visited.append(start)
    for node in graph[start]:
        dfs_recursive(graph, node, visited)
    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']}

print(dfs_iterative(graph, 'A'))
print(dfs_recursive(graph, 'A'))
