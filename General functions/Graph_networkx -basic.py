import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()


# ADD NODES
#G.add_node('A')
#G.add_nodes_from(['B','C','D'])

# ADD EDGES
#G.add_edge('A','B')
G.add_edges_from([('A','C'),('A','D'),('B','E')])
#G.add_weighted_edges_from([('A','B',2),('A','C',3),('B','D',4),('B','E',5)])

#PRINT DANH SÁCH KỀ, BẬC
#print('G.adj: ',G.adj)
#print('Degree A: ',G.degree('A'))

# VẼ ĐỒ THỊ
nx.draw(G)
plt.show()
'''pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_weight)
plt.show()'''
#plt.savefig('drawGraph.png')
#GP = nx.petersen_graph()
#nx.draw(GP,with_labels=True,font_weight='bold')
#plt.show()


def drawGraph(graph):
    # import ở đầu 2 dòng:
    # import networkx as nx
    # import matplotlib.pyplot as plt

    #truyền vào G với 2 thuộc tính: g.vertexes và g.edges với format:
    # G.vertexes = ['A','B','C']
    # G.edges = {('A','B'): 5,('B','A'): 5, ('B','C'): 1, ('C','B'): 1}

    graphDraw = nx.Graph()
    for a,b in graph.edges.items():
        graphDraw.add_weighted_edges_from([(a[0], a[-1], b)])
    pos = nx.spring_layout(graphDraw)
    nx.draw(graphDraw, pos, with_labels=True, font_weight='bold')
    edge_weight = nx.get_edge_attributes(graphDraw, 'weight')
    nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edge_weight)
    plt.show()

def drawGraphNotWeight(graph):
    # import ở đầu 2 dòng:
    # import networkx as nx
    # import matplotlib.pyplot as plt

    #truyền vào G với 2 thuộc tính: g.vertexes và g.edges với format:
    # G.vertexes = ['A','B','C']
    # G.edges = [('A','B'),('B','A'), ('B','C'),('C','B')]

    graphDraw = nx.Graph()
    graphDraw.add_edges_from(graph.edges)
    nx.draw(graphDraw)
    plt.show()