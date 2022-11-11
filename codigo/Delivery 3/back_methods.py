import dijkstra
import pandas as pd
import math
import time
    
def information(dictionary):
    
    origin = dictionary['origin']
    destination = dictionary['destination']
    return origin, destination

def dataframe_creation():
    
    dataframe = pd.read_csv('calles_de_medellin_con_acoso.csv', sep = ';')
    return dataframe
    

def graph_creation(dataframe):

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
        
        # This variable is a tri-tuple that contains the length, harassment risk and a combination ob both that will be used latter
        weight = (
                    dataframe["length"][i],
                    dataframe["harassmentRisk"][i],
                    (dataframe["length"][i] + dataframe["harassmentRisk"][i])/3,
                    pow(dataframe["length"][i], dataframe["harassmentRisk"][i]) * dataframe["harassmentRisk"][i],
                    (dataframe["length"][i] * math.tau) + (dataframe["harassmentRisk"][i] * 1000)
                )

        # Storing the variable in the graph
        graph[dataframe["origin"][i]][dataframe["destination"][i]] = weight
        
        # Checking whether it is oneway, if it is, we will create a new origin taking the destination
        if dataframe["oneway"][i]==True:
            try:
                graph[dataframe["destination"][i]][dataframe["origin"][i]] = weight
            except KeyError:
                graph[dataframe['destination'][i]] = {dataframe["origin"][i]:weight}
    
    return graph


def path(graph, origin, destination, option):

    start = time.perf_counter()
    path, total_distance, average_risk = dijkstra.dijkstra(graph, origin, destination, option) 
    end = time.perf_counter()
    final_time = (end - start)
    
    print(f' -- Path {option - 1} --')
    print(f"path {option - 1} time -> {final_time:.03f} secs.")
    print(f'total distance -> {total_distance:.03f}')
    print(f'average risk -> {average_risk:.03f} \n')
    
    return path, final_time
        
        
# Origin is a coordinate given by Google Maps and we find the nearest place in the dataframe.
def nearest_origin(origin, dataframe):

    distance = float('infinity')
    nearest_coordinate = ()
    
    for coordinate in dataframe['origin']:
        
        longitude, latitude = list(map(float, coordinate[1:-1].split(',')))
        
        current_distance = haversine_distance(origin, (latitude, longitude))
    
        if current_distance < distance:
            distance = current_distance
            nearest_coordinate = (latitude, longitude)
    
    return str((nearest_coordinate[1],nearest_coordinate[0]))  


# Destination is a coordinate given by Google Maps and we find the nearest place in the dataframe.
def nearest_destination(destination, dataframe):

    distance = float('infinity')
    nearest_coordinate = ()
    
    for coordinate in dataframe['destination']:
        
        longitude, latitude = list(map(float, coordinate[1:-1].split(',')))
        
        current_distance = haversine_distance(destination, (latitude, longitude))
    
        if current_distance < distance:
            distance = current_distance
            nearest_coordinate = (latitude, longitude)
    
    return str((nearest_coordinate[1],nearest_coordinate[0]))    


# Calculate the distance between two points in a sphere
def haversine_distance(origin, destination):

    latitude_1, longitude_1 = origin
    latitude_2, longitude_2 = destination
    radius = 6500

    new_latitude = math.radians(latitude_2 - latitude_1)
    new_longitude = math.radians(longitude_2 - longitude_1)
    
    side_a = (math.sin(new_latitude / 2) * math.sin(new_latitude / 2) + math.cos(math.radians(latitude_1)) * math.cos(math.radians(latitude_2)) * math.sin(new_longitude / 2) * math.sin(new_longitude / 2))
    side_c = 2 * math.atan2(math.sqrt(side_a), math.sqrt(1 - side_a))
    distance = radius * side_c

    return distance


def print_time(time_1, time_2, time_3 = 0):
    
    total_time = time_1 + time_2 + time_3
    
    if time_3 != 0: print(f'Dijkstra total time is -> {total_time:.03f} secs.\n')
    else: print(f'Program total time is -> {total_time:.03f} secs.\n')
    

def ask_continue():
    
    if input('Want to continue? (Y/n): ') == 'Y': return True
    else: return False