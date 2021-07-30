import networkx as nx
import numpy as np 
import random
import operator
import matplotlib.pyplot as plt


def random_walk(G):
    '''
        Random walk creation
        :params: G original graph
    '''
    
    # number of vertices
    n = nx.number_of_nodes(G)
    
    # initial vertex chosen at random
    first_node = random.randint(0, n-1)
    
    # visited vertices parameter
    is_visited = np.zeros(n, dtype=bool)
    
    # map the first visit to each vertex
    first_visit = np.zeros(n, dtype=int)
    
    # set first node to visited
    is_visited[first_node] = True
    
    # choose a random neighbor
    neighbor = np.random.choice(list(G.neighbors(first_node)))
    
    # set neighbor to visited
    is_visited[neighbor] = 1

    # update the first visit of the first node and their neighbor
    first_visit[first_node] = neighbor
    first_visit[neighbor] = first_node
    
    # counting the number of visited nodes
    count_nodes = 2
    while True:
        
        # set the last node visited
        last_node = neighbor
        
        # choose a neighbor at random
        curr_neighbor = np.random.choice(list(G.neighbors(neighbor)))
        
        # if the neighbor is not visited yet
        if not is_visited[curr_neighbor]:
            # set the first visit the last_node 
            first_visit[curr_neighbor] = last_node
            # set current neighbor to visited
            is_visited[curr_neighbor] = 1
            count_nodes = count_nodes + 1
        
        # if visited all the nodes, stop
        if count_nodes == n:
            break  
        
        # set neighbor to curr_neighbor
        neighbor = curr_neighbor
        
    return first_visit, first_node

def generate_random_tree(G):
    # run the random walk
    first_visit, first_node = random_walk(G)
    
    # initialize an empty tree
    random_tree = nx.Graph()
    
    # fill the graph with (j,i) edges from first_visit for all i != first_node
    for i in range(len(first_visit)):
        if i != first_node:
            random_tree.add_edge(first_visit[i], i)

    return random_tree

