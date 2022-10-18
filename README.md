# Last contribution:

## Code for second delivery

This folder has 5 files. Two with the information to build the graph and plot, and three that have the code.
You need to download all files, but **only run the 'main.py'** to see the result.

### Graph methods
There you will see 3 functions.
  - Graph creation: Creates the graph as an adjacency list built with dictionaries and fills it with the information of "*calles_de_medellin_con_acoso.csv*".
  - Dijkstra: The algorithm that makes the route. Returns a dictionary with the previous vertices (to build the path with 'Generate path') and a queue.
  - Generate path: A recursive function that stores the data of the dictionaries that returns the Dijkstra algorithm in the queue given also by Dijkstra.
  
### Graphics
There you will see 2 functions.
  - Plot path: Uses the Google Maps engine with the library gmplot to plot the path given by the function 'generate_path' in 'graph_methods.py'.
  - Alert: Explains some things that appear in the plot gmplot generates.


> If any question, write to Manuela Castaño Franco (mcastanof1@eafit.edu.co) or Santiago Neusa Ruiz (sneusar@eafit.edu.co).
