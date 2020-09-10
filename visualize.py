#   to output visual networks

import mod_degroot
import make_matrix

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import visualize
import scipy

#================   Drawing simple NETWORK     ========================
def network(network_matrix):
    rows, cols = np.where(network_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    graph = nx.Graph()
    graph.add_edges_from(edges)
    nx.draw(graph, node_size=500, with_labels=True)
    print("Drawing network matrix")
    plt.show()


#network with colors representing friendcount
def network_friendcount(network_matrix,n):
    rows, cols = np.where(network_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    graph = nx.Graph()
    graph.add_edges_from(edges)
    pos = nx.spring_layout(graph, iterations=200)

    nx.draw(graph, pos, node_color=range(n), node_size=800, cmap=plt.cm.Reds, with_labels=True)
    plt.show()

#network with colors representing opinion
def network_opinion_colors(network_matrix, opinion_matrix):
    graph = nx.Graph(network_matrix)

    pos = nx.spring_layout(graph, iterations=2)

    labels = {i: round(opinion_matrix[i],3) for i in range(0, len(opinion_matrix))}

    #color_map = np.array(opinion_matrix)
    color_map = [labels.get(node, 0.25) for node in graph.nodes()]

    nx.draw(graph, pos, node_size=800, cmap=plt.get_cmap('viridis'),vmin=0, vmax=1,node_color=color_map)
    nx.draw_networkx_labels(graph, pos, labels, font_size=10)

    plt.show()

    return graph



#====    MIDTERM   draw histogram with final opinion by decimal  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_value_ratio(n, matrix_network, matrix_weight, n_conversations, n_issues, visualize_rate):

    final_opinion_array = [] #array containing average final opinion

    #calculate final opinions for n_issues
    for x in range (n_issues):
        matrix_opinion = make_matrix.opinion(n)
        #matrix_opinion[0] = 0.9
        matrix_opinion_new = mod_degroot.opinion(n, matrix_network, matrix_weight, matrix_opinion, n_conversations, visualize_rate)
        final_opinion_array.append(round(np.mean(matrix_opinion_new),1))
        #print("\n>> Final Opinion Matrix after", n_conversations, "conversations on issue number",x+1,":\n", matrix_opinion_new)
        #print("Final Opinion Array",final_opinion_array)


    visualize.plot_bar_graph(final_opinion_array)

    return 0


#  a list of visualization code that works, for reference purposes
def lists_of_code(network_matrix,opinion_matrix):
    #  draw graph from adj matrix
    graph = nx.Graph(network_matrix)
    nx.draw(graph)
    plt.show()

    #converting matrix into dictionary to use as labels
    labels = {i: opinion_matrix[i] for i in range(0, len(opinion_matrix))}

    #   make color map
    color_map = np.array(opinion_matrix)


def plot_bar_graph(array):
    # plotting bar graph

    plt.hist(array)
    plt.xlabel('Average Opinion at Consensus', fontsize=10)
    plt.ylabel('No of Occurrences', fontsize=10)

    plt.show()

def scatterplotthis(xvals,yvals,xlabel="Original opinion",ylabel="Final self-weight"):
    plt.scatter(xvals, yvals)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)

    plt.show()


