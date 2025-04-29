from collections import deque

def bfs(graph, start_node):
    """
    Perform Breadth-First Search on a graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph
        start_node: Node to start the search from
        
    Returns:
        dict: Dictionary containing the parent of each node in the BFS tree
    """
    visited = set()
    parent = {start_node: None}
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        current_node = queue.popleft()
        
        # Process the current node here
        # YOUR BFS PROCESSING CODE GOES HERE
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)
    
    return parent

def dfs(graph, start_node):
    """
    Perform Depth-First Search on a graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph
        start_node: Node to start the search from
        
    Returns:
        dict: Dictionary containing the parent of each node in the DFS tree
    """
    visited = set()
    parent = {start_node: None}
    
    def dfs_helper(node):
        visited.add(node)
        
        # Process the current node here
        # YOUR DFS PROCESSING CODE GOES HERE
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                dfs_helper(neighbor)
    
    dfs_helper(start_node)
    return parent

# Example usage:
if __name__ == "__main__":
    # Example graph (adjacency list)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("BFS Parent pointers:", bfs(graph, 'A'))
    print("DFS Parent pointers:", dfs(graph, 'A'))