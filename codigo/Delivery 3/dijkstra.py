from collections import deque
import heapq

# Algorithms to reduce both distance and harassment risk

# Version 1
def dijkstra(graph, origin, destination, option):
    
    # Creating dictionaries and initializing their values
    distances = {vertex: float('infinity') for vertex in graph}
    risks = {vertex: float('infinity') for vertex in graph}
    melted = {vertex: float('infinity') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    
    # The origin doesn't have distance to itself or a predecesor, so we make sure to set that values
    distances[origin] = 0
    risks[origin] = 0
    melted[origin] = 0
    previous[origin] = None 

    # Creating the priority queue and assigning a tuple
    priority_queue = [(distances[origin], risks[origin], melted[origin], origin)]
    
    
    while len(priority_queue) > 0:
        
        distance, risk, melt, current_node = heapq.heappop(priority_queue)

        if current_node == destination: break
        
        # As each origin (current_node) has many destinations, we iterate in those destinations (adjacent_node)
        for adjacent_node in graph[current_node]:
            
                                                 # This is the third variable we stored in the weight while creating the graph
            distance = distances[current_node] + graph[current_node][adjacent_node][0]
            risk = risks[current_node] + graph[current_node][adjacent_node][1]
            melt = melted[current_node] + graph[current_node][adjacent_node][option]
            
            if melt < melted[adjacent_node]:
                
                # Updating to new values and saving the information in the priority queue
                distances[adjacent_node] = distance
                risks[adjacent_node] = risk
                melted[adjacent_node] = melt
                previous[adjacent_node] = current_node
                heapq.heappush(priority_queue, (distance, risk, melt, adjacent_node))
    
    
    # This is a variable to plot the path
    path = deque()  
    generate_path(previous, destination, path)        
    
    return path, distances[destination], risks[destination]/len(path)


# This is a function to build the path
def generate_path(previous, current, path):
    
    if previous[current] == None:
        path.appendleft(current)
        return path
    else:
        path.appendleft(current)
        return generate_path(previous, previous[current], path) 