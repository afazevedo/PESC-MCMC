import networkx as nx
import numpy as np 
import math
import random

class NodeGenerator:
    
    def __init__(self, original_graph, spanning_tree):
        self.original_graph = original_graph
        self.spanning_tree = spanning_tree
        
    def generate(self):
    #     '''
    #     Creates a new graph by adding a G-T edge and removing an edge from the cycle.
    #     :param graph: networkx graph
    #     :return: networkx graph
    #     '''
        
        edges_original_graph = list(self.original_graph.edges) # set of original graph edges
        edges_spanning_tree = list(self.spanning_tree.edges) # set of tree edges
        
        nonedges_spanning_tree = list(nx.non_edges(self.spanning_tree))  # set of non-T edges
        A = list(set(edges_original_graph) & set(nonedges_spanning_tree)) # set of non-T edges of G

        # choose an edge from the nonedges set and add it to the graph forming a cycle
        chosen_A = random.choice([x for x in A])
        self.spanning_tree.add_edge(chosen_A[0], chosen_A[1])

        # choose an edge of the cycle and remove it from the graph
        chosen_B = random.choice([x for x in nx.find_cycle(self.spanning_tree)])
        self.spanning_tree.remove_edge(chosen_B[0], chosen_B[1])
        
        
        return self.spanning_tree