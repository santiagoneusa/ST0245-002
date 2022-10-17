import graph_methods as gm
import graphics


def main():
    
    graph = gm.graph_creation()

    print('The coordinates that will be used to create the path are from EAFIT and U. de Medellín.\n')
    origen = "(-75.5778046, 6.2029412)"
    destino = "(-75.6101004, 6.2312125)"

    previous, path = gm.dijkstra_distance_and_risk(graph, origen, destino) 

    path = gm.generate_path(previous, destino, path)
    
    graphics.alert()
    graphics.plot_path(path)

main()