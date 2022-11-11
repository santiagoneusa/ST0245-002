import gmplot
import pandas as pd
import webbrowser

# the function to plot the paths and the alerts shown in terminal

 
def alert():
    
    white_start = '\33[7m'
    white_end = '\033[0m'
    print(white_start + 'The circles on the path are the intersections between the streets' + white_end, '\n')
    
    red_start = '\33[41m'
    red_end = '\033[0m'
    print(red_start + "The red line is the path 1." + red_end)
    blue_start = '\33[44m'
    blue_end = '\033[0m'
    print(blue_start + "The blue line is the path 2." + blue_end)
    violet_start = '\33[45m'
    violet_end = '\033[0m'
    print(violet_start + "The violet line is the path 3." + violet_end)
    print()
    
    
def plot_paths(path_1, path_2, path_3, API_key):
    
    latitude_limit, longitude_limit = medellin_edges()
    
    latitude_1, longitude_1 = organize_coordinates(path_1)
    latitude_2, longitude_2 = organize_coordinates(path_2)
    latitude_3, longitude_3 = organize_coordinates(path_3)
    
    file = gmplot.GoogleMapPlotter(6.267203842477565, -75.579710387, 12, apikey = API_key)
    
    file.polygon(latitude_limit, longitude_limit, face_color = 'black', face_alpha = 0.3, edge_color='black', edge_width = 6)
    
    # Ploting path 1
    file.scatter(latitude_1, longitude_1, 'deepskyblue', size = 2, marker = False)
    file.plot(latitude_1,longitude_1,'deepskyblue',edge_width = 9)
     
    # Ploting path 2
    file.scatter(latitude_2,  longitude_2, 'yellowgreen', size = 2, marker = False)
    file.plot(latitude_2,  longitude_2, 'yellowgreen', edge_width = 9)
    
    # Ploting path 3
    file.scatter(latitude_3,longitude_3,'gold', size = 2, marker = False)
    file.plot(latitude_3,longitude_3,'gold',edge_width = 9)
    
    file.marker(latitude_1[0], longitude_1[0], label = 'A', title = 'Starting Point')
    file.marker(latitude_1[-1], longitude_1[-1], label = 'B', title = 'End Point')
    
    file.draw("dijkstra_distance_and_risk.html")
    
    # Opening the .html file for you ;)
    webbrowser.open_new_tab('dijkstra_distance_and_risk.html')
    
    
def medellin_edges():
    
    longitudes_array = []
    latitudes_array = []
    
    area = pd.read_csv('poligono_de_medellin.csv',sep=';')
    polygon = str(area['geometry'].to_list()[0])[9:-2].split(',')
    
    for coord in polygon:
        longitude, latitude = list(map(float,coord[1:].split(' ')))
        longitudes_array.append(longitude)
        latitudes_array.append(latitude)
        
    return latitudes_array, longitudes_array 


def organize_coordinates(path):
    
    longitude = []
    latitude = []
    
    while len(path) > 0:
        
        coordinate = path.pop()
        # The coordinates enter as a string, so here we slice and convert the strings to floats
        coordinate = coordinate[1:-1].split(', ')
        
        # And as the latitude and longitude are inverted in the dataframe, we fix that
        longitude.append(float(coordinate[0]))
        latitude.append(float(coordinate[1]))
    
    return latitude, longitude