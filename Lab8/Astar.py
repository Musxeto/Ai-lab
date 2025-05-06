import heapq

graph = {
    0: [(1, 1), (2, 1)],  # From 0, go to 1 or 2, each with cost 1
    1: [(0, 1), (3, 1)],  # From 1, go to 0 or 3, each with cost 1
    2: [(0, 1), (3, 1)],  # From 2, go to 0 or 3, each with cost 1
    3: [(1, 1), (2, 1), (4, 1)],  # From 3, go to 1, 2, or 4, each with cost 1
    4: [(3, 1)]           # From 4, go back to 3, with cost 1 (goal)
}

heuristic_map = {
    0: 3,  # Estimated cost from 0 to goal
    1: 2,  # Estimated cost from 1 to goal
    2: 2,  # Estimated cost from 2 to goal
    3: 1,  # Estimated cost from 3 to goal
    4: 0   # Goal node, no cost to reach goal
}

def a_star(graph, heuristic_map, start, goal):
    open_set = []
    heapq.heappop(open_set,(heuristic_map[start],start))

    g_cost = {}

    # initialize all nodes to infinity and start to zero
    for node in graph:
        g_cost[node] = float('inf')
    
    g_cost[start] = 0

    came_from = {}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            total_distance = g_cost[current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, total_distance
        
        for neighbor, cost in graph[current]:
            t_cost = g_cost[current] + cost

            if t_cost < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = t_cost
                f_cost = t_cost + heuristic_map[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor))
    return None, float('inf')  # No path found
if __name__ == "__main__":
    start_node = 0
    goal_node = 4
    path, total_distance = a_star(graph, heuristic_map, start_node, goal_node)
    if path:
        print(f"Path found: {path} with total distance: {total_distance}")
    else:
        print("No path found")
# This code implements the A* search algorithm to find the shortest path in a graph.        