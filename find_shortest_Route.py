def dijkstra(graph, start, end):
    # Initialize distances to infinity for all nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize previous nodes to None
    previous = {node: None for node in graph}
    
    # List to keep track of visited nodes
    visited = []
    
    # Loop through all nodes
    while len(visited) < len(graph):
        # Find the node with the smallest distance
        min_distance_node = None
        min_distance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_distance_node = node
        
        # If no node found, exit loop
        if min_distance_node is None:
            break
        
        # Mark the node as visited
        visited.append(min_distance_node)
        
        # Update distances to neighboring nodes
        for neighbor, weight in graph[min_distance_node].items():
            distance = distances[min_distance_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = min_distance_node
    
    # Reconstruct the shortest path
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous[current_node]
    path.reverse()
    
    return path

def main():
    # Example input graph
    graph_data = {
        "nodes": {
            "a": {"label": "a", "x": -80, "y": -120},
            "b": {"label": "b", "x": -80, "y": -40},
            "c": {"label": "c", "x": 0, "y": -120},
            "d": {"label": "d", "x": 0, "y": -40},
            "e": {"label": "e", "x": 80, "y": -120},
            "f": {"label": "f", "x": 80, "y": -40}
        },
        "edges": [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"], ["e", "f"]]
    }
    
    # Convert graph data to graph representation
    graph = {}
    for edge in graph_data["edges"]:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        # Assuming each edge has a weight of 1
        graph[node1][node2] = 1
        graph[node2][node1] = 1  # Undirected graph
    
    # Example: find shortest route from "a" to "f"
    start_node = "a"
    end_node = "f"
    shortest_route = dijkstra(graph, start_node, end_node)
    
    print("Shortest route from", start_node, "to", end_node, ":", shortest_route)

if __name__ == "__main__":
    main()
