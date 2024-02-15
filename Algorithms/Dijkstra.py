import heapq


def dijkstra(graph, start):

    # initializer distances from start to all nodes as infinity

    distances = {vertex: float('infinity') for vertex in graph}

    '''
    distances = {vertex: float('infinity') for vertex in graph}
    
        This ^ is an example of dictionary comprehension:
        a concise way of creating dictionaries in an iterative manner 
        
        The following line:
        
        vertex: float('infinity') 
            ^This sets the value of each key within the dictionary
            
            for vertex in graph
                iterates over all keys within the graph dictionary
            
            !! Each key within the graph is node from the graph.
            Where each value associated to the key is a distance: 
                which is initially assigned the value 'infinity' 

    '''

    distances[start] = 0
    # We set the start value to 0, since this represents the distance from the start

    priority_queue = [(0, start)]
    # PQ initialized with the starting distance (0,start)
    # The priority of the tuple is determined by the first element within the tuple
    # However in the event that the first elements are equal, then the PQ will compare the second elements


    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Example usage
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")