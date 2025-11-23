from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Invalid nodes
    if start not in graph or goal not in graph:
        return []

    # Trivial case
    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        curr = queue.popleft()

        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = curr
                queue.append(nxt)

                if nxt == goal:
                    # Reconstruct the path
                    path = []
                    node = goal
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return list(reversed(path))

    return []
