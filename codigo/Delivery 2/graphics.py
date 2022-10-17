import gmplot
import webbrowser


def plot_path(path):
    
    # The arrays store the coordinates because gmplot uses arrays to read the information
    longitude = []
    latitude = []
    
    while len(path) > 0:
        
        coordinate = path.pop()
        # The coordinates enter as a string, so here we slice and convert the strings to floats
        coordinate = coordinate[1:-1].split(', ')
        
        # And as the latitude and longitude are inverted in the dataframe, we fix that
        longitude.append(float(coordinate[0]))
        latitude.append(float(coordinate[1]))
    
    # Creating the plot with Google Maps engine
    file = gmplot.GoogleMapPlotter(6.2115169,-75.5728593, 14)
    
    file.scatter( latitude, longitude, '#FFFFFF', size = 7, marker = False )
    file.plot(latitude, longitude, 'indianred', edge_width = 7)
    
    file.draw( "dijkstra_distance_and_risk.html" )
    # Opening the .html file for you ;)
    webbrowser.open_new_tab('dijkstra_distance_and_risk.html')
 
 
def alert():
    
    white_start = '\33[7m'
    white_end = '\033[0m'
    print(white_start + 'The white circles on the path are the intersections between the streets' + white_end, '\n')
    
    red_start = '\33[41m'
    red_end = '\033[0m'
    print(red_start + "The red line is the path." + red_end)
    
    