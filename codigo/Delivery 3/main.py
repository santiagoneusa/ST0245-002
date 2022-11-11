import back_methods as bm
import graphics
import server
import gui
import time


def main():
    
    dataframe = bm.dataframe_creation()
    graph = bm.graph_creation(dataframe)
    
    API_key_verification = server.alert_API_key()
    
    while True:  
                  
        if API_key_verification:
                    
            origin_gui, destination_gui = bm.information(gui.interface())
            
            API_key = server.get_API_key()
            url_service, settings = server.initialize_connection(API_key)
                    
            # Searching places
            origin = bm.nearest_origin(server.search_place(origin_gui, API_key, url_service, settings), dataframe)
            destination = bm.nearest_destination(server.search_place(destination_gui, API_key, url_service, settings), dataframe)

            # Creating paths
            path_1, time_1 = bm.path(graph, origin, destination, 2)
            path_2, time_2 = bm.path(graph, origin, destination, 3)
            path_3, time_3 = bm.path(graph, origin, destination, 4)
                    
            graphics.alert()
            bm.print_time(time_1, time_2, time_3)
                    
            # Plotting paths
            graphics.plot_paths(path_1, path_2, path_3, API_key)
            
            if bm.ask_continue() is False: break
            
        else: break
            
    print('Goodbye.')

start = time.perf_counter()
main()
end = time.perf_counter()
bm.print_time(start, end)