#Libraries
import pandas as pd
import heapq
from collections import deque


def graph_creation():

    # Dataframe creation: Reading the csv file
    dataframe = pd.read_csv('calles_de_medellin_con_acoso.csv', sep = ';')

    # Fill None values in harrasmentRisk column
    dataframe.harassmentRisk.fillna(dataframe.harassmentRisk.mean(), inplace = True)

    # Delete duplicated origins
    unique_origins = dataframe.origin.unique()

    # Graph creation
    graph = {}

    # Fill the graph
    for i in range(len(unique_origins)): graph[unique_origins[i]] = {}

    # This part 
    for i in dataframe.index:
        
        # This variable is a tri-tuple that contains the length, harassment risk and a combination of both that will be used later
        weight = (dataframe["length"][i], dataframe["harassmentRisk"][i], (dataframe["length"][i]+dataframe["harassmentRisk"][i])/2)

        # Storing the variable in the graph
        graph[dataframe["origin"][i]][dataframe["destination"][i]] = weight
        
        # Checking whether it is oneway, if it is, we will create a new origin taking the destination
        if dataframe["oneway"][i]==True:
            try:
                graph[dataframe["destination"][i]][dataframe["origin"][i]] = weight
            except KeyError:
                graph[dataframe['destination'][i]] = {dataframe["origin"][i]:weight}
    
    return graph
           
           
# Algorithm to reduce both distance and harassment risk
def dijkstra_distance_and_risk(graph, origin, destination):
    
    # Creating dictionaries and initializing their values
    distances = {vertex: float('infinity') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    
    # The origin doesn't have distance to itself or a predecesor, so we make sure to set that values
    distances[origin], previous[origin] = 0, None 

    # Creating the priority queue and assigning a tuple
    priority_queue = [(distances[origin], origin)]
    
    
    while len(priority_queue) > 0:
        
        distance, current_node = heapq.heappop(priority_queue)

        if current_node == destination: break
        
        # As each origin (current_node) has many destinations, we iterate in those destinations (adjacent_node)
        for adjacent_node in graph[current_node]:
            
                                                 # This is the third variable we stored in the weight while creating the graph
            distance = distances[current_node] + graph[current_node][adjacent_node][2]
            
            if distance < distances[adjacent_node]:
                
                # Updating to new values and saving the information in the priority queue
                distances[adjacent_node] = distance
                previous[adjacent_node] = current_node
                heapq.heappush(priority_queue, (distance, adjacent_node))
    
    
    # This is a variable to plot the path
    path = deque  ()          
    
    return previous, path


def generate_path(previous, current, path):
    
    if previous[current] == None:
        path.appendleft(current)
        return path
    else:
        path.appendleft(current)
        return generate_path(previous, previous[current], path) 
