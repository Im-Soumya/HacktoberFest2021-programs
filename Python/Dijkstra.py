def dijkstra():
    nodes = int(input("Enter the number of nodes in the graph: "))
    graph = {}
    for _ in range(nodes):
        key = input("Enter the node value: ")
        values = input("Enter the nodes it is connected to along with the weight in a tuple: ").split(',')
        values = [(node_weight[0], int(node_weight[1])) for node_weight in (value.split(':') for value in values)]
        graph[key] = values
    source = input("Enter the source for minimum spanning tree: ")
    visited = set()
    visited.add(source)
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    def get_min_distance_node(distances, visited):
        min_distance = float('inf')
        min_node = None
        for node in distances:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        return min_node
    
    while len(visited) < len(graph):
        current_node = get_min_distance_node(distances, visited)
        if current_node is None:
            break  
        visited.add(current_node)
        if current_node not in graph:
            continue  
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance 
    return distances

distances = dijkstra()
print("Shortest distances from the source:")
for node in distances:
    print(f"{node}: {distances[node]}")
