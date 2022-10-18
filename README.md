# Last contribution:

## Code for second delivery

This folder has 5 files. Two with the information to build the graph and plot, and three that have the code.
You need to download all files, but **only run the 'main.py'** to see the result.

### Graph methods
There you will see 3 functions.
  - Graph creation: create the graph as an adjacency list build with dictionaries and fill with the information of "*calles_de_medellin_con_acoso.csv*".
  - Dijkstra: the algorithm that makes the route. Return a dictionarie with the previouses vertex (to build the path with 'Generate path') and a queue.
  - Generate path: A recursive function that stores the data of the dictionarie that returns the Dijkstra algorithm in the queue given also by Dijkstra.
  
### Graphics
There you will see 2 functions.
  - Plot path: uses the Google Maps engine with the librarie gmplot to plot the path given by the function 'generate_path' in 'graph_methods.py'.
  - Alert: Explain the some things that appear in the plot gmplot generates.


> If any question, write to Manuela Castaño Franco (mcastanof1@eafit.edu.co) or Santiago Neusa Ruiz (sneusar@eafit.edu.co).
