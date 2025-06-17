from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

def bfs(graph,start,end):
    if start not in graph or end not in graph:
        print("Specified Start or End is not in the graph")
        return
    
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node == end:
            print(node, end=' ')
            print(f"Path found from {start} to {end}.")
            return
        if node not in visited:
            visited.add(node)
            print(node, end='->')
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    print(f"No path found from {start} to {end}.")


print("Graph:", graph)
bfs(graph, 'A', 'G')


