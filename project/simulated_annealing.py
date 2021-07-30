import networkx as nx
from initial_solution import *
import numpy as np 
import math
import random
from nodes_generator import NodeGenerator
import matplotlib.pyplot as plt
import time
import os
class SimulatedAnnealing:
    def __init__(self, original_graph, initial_temp, alpha, stopping_temp, stopping_iter, matrix_cost, B, start_time):
        ''' 
            Parameters
            ----------
            original_graph: nx.graph
                original graph G
            initial_temp: float
                initial temperature
            alpha: float
                rate at which temp decreases
            stopping_temp: float
                temperature at which annealing process terminates
            stopping_iter: int
                interation at which annealing process terminates
            matrix_cost: array like
                original cost from G
            B: float
                budget from source data
            start_time: float 
                start time execution
        '''
        
        # set simulated annealing parameters
        self.temp = initial_temp # set temperature to initial temperature
        self.initial_temp = initial_temp
        self.alpha = alpha 
        self.stopping_temp = stopping_temp
        self.stopping_iter = stopping_iter
        self.start_time = start_time
        
        # set initial parameters
        self.iteration = 0
        self.original_graph = original_graph
        self.dist_matrix = matrix_cost
        self.budget = B
        self.curr_solution = generate_random_tree(self.original_graph) #initial solution
        self.best_solution = nx.Graph.copy(self.curr_solution)
        
        if self.calculate_diameter(self.best_solution) <= self.budget:
            self.best_diameter = self.calculate_diameter(self.best_solution)
        else:
            self.best_diameter = 10000000
        
        # set initial weight parameters
        self.curr_weight = self.weight(self.curr_solution)
        aux_weight = self.curr_weight
        self.initial_weight = aux_weight

        # set initial diameter parameters
        self.curr_diameter = self.calculate_diameter(self.curr_solution)
        aux_diameter = self.curr_diameter
        self.initial_diameter = aux_diameter

        # set initial list parameters
        self.weight_list = [aux_weight]
        self.diameter_list = [aux_diameter]
        self.solution_history = [initial_temp]
        
        if self.curr_weight <= self.budget:
            self.best_solution_history_diameter = [self.curr_diameter]
            self.best_solution_history_weight = [self.curr_weight]
        else:
            self.best_solution_history_diameter = []
            self.best_solution_history_weight = []
        
        # print initial log
        print('===================================')
        print('Initial weight: ', aux_weight)
        print('Initial diameter: ', aux_diameter)
        print('=====================================')
        
    def weight(self, candidate):
        '''
        Calculate weight
        '''
        total_cost = 0
        for i,j in candidate.edges():
            total_cost += self.dist_matrix[i,j]

        return total_cost

    def calculate_diameter(self, candidate):
        '''
        Calculate diameter
        '''
        return nx.diameter(candidate, e=None, usebounds=False)
    
    def acceptance_probability(self, candidate_diameter):
        '''
        Acceptance probability using boltzmann:
        '''
        return math.exp(-abs(candidate_diameter - self.curr_diameter) / self.temp)

    def local_search(self, spanTree):
        n = nx.Graph.number_of_nodes(spanTree)
        C = self.dist_matrix
        B = self.budget
        
        viavel = False
        L = n//2
        labelNodes = np.zeros(n)

        spanCost = self.weight(spanTree)

        while True:
            improve = False

            for k in range(L):
                node_center = nx.algorithms.distance_measures.center(spanTree)
                if len(node_center) < 2:
                    minPathleft, path = nx.single_source_bellman_ford(spanTree, node_center[0])
                    for node in range(n):
                        labelNodes[node] = minPathleft[node] 
                else:
                    minPathleft, path = nx.single_source_bellman_ford(spanTree, node_center[0])
                    minPathRight, path = nx.single_source_bellman_ford(spanTree,node_center[1])
                    
                    for node in range(n):
                        if minPathleft[node] < minPathRight[node]:
                            labelNodes[node] = minPathleft[node]
                        else:
                            labelNodes[node] = minPathRight[node]
                lcr = []
                for i in range(n):
                    if labelNodes[i] == k:
                        lcr.append(i)

                if len(lcr) > 0:
                    chegada = np.zeros(n, dtype=bool)
                    for i in lcr:
                        greatBenefit = 10000 
                        greatInd = -1 
                        node_chose = -1
                        
                        neighbors = nx.all_neighbors(spanTree, i)
                        for j in neighbors:
                            if labelNodes[j] <= labelNodes[i] and nx.Graph.has_edge(spanTree, i,j):
                                node_chose = j 
                            
                        for j in range(n):
                            if C[i,j] > 0000.1 and node_chose != -1 and i != j and node_chose != j and C[node_chose, i] > C[i,j] and (C[i,j] - C[node_chose, i]) < greatBenefit and not nx.Graph.has_edge(spanTree, i,j) and not chegada[i]:
                                greatBenefit = C[i,j] - C[node_chose, i]
                                greatInd = j 
                                
                        if greatInd != -1:
                            aux_tree = nx.Graph.copy(spanTree)
                            aux_cost = self.weight(aux_tree)
                            
                            spanCost = spanCost + (C[i,greatInd] - C[node_chose, i])
                            nx.Graph.add_edge(spanTree, i, greatInd)
                            nx.Graph.remove_edge(spanTree, node_chose, i)
                            
                            if nx.is_connected(spanTree):
                                chegada[greatInd] = 1
                                labelNodes[i] = labelNodes[greatInd] + 1
                                if spanCost + (C[i,greatInd] - C[node_chose, i]) <= spanCost:
                                    improve = True
                                # print("custo caiu!", spanCost)
                            else:
                                aux_2_tree = nx.Graph.copy(aux_tree)
                                aux_2_cost = aux_cost
                                spanTree = aux_2_tree
                                spanCost = aux_2_cost
                                
                            if spanCost <= B:
                                viavel = True 
                                d = nx.diameter(spanTree) 
                                return spanTree
                if viavel or not improve:
                    return spanTree 
    
    def accept(self, candidate):
        '''
        Accept with probability 1 if candidate solution is better than
        current solution, else accept with probability equal to the
        acceptance_probability()
        '''
        
        # calculate f and g    
        candidate_diameter = self.calculate_diameter(self.curr_solution)
        candidate_weight = self.weight(self.curr_solution)
    
    
        # if the diameter of the neighbor is smaller or equal but with a smaller weight, we accept    
        if candidate_diameter < self.curr_diameter or (candidate_diameter == self.curr_diameter and candidate_weight < self.curr_weight):
            
            # update best solution and history
            if candidate_weight <= self.budget and candidate_diameter <= self.best_diameter:
                current = nx.Graph.copy(candidate)
                self.best_solution = current
                self.best_diameter = self.calculate_diameter(current)
                self.best_solution_history_diameter.append(self.calculate_diameter(current))
                self.best_solution_history_weight.append(self.weight(current))

            # update current solutions
            self.curr_diameter = candidate_diameter
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
        else:
            # if not, we will accept according to boltzmann distribution
            unif = random.random() # generate a uniform number between 0 and 1
            if unif < self.acceptance_probability(candidate_diameter):
                
                # updates the best solution and history
                if candidate_weight <= self.budget and candidate_diameter <= self.best_diameter:
                    current = nx.Graph.copy(candidate)
                    self.best_solution = current
                    self.best_diameter = self.calculate_diameter(current)
                    self.best_solution_history_diameter.append(self.calculate_diameter(current))
                    self.best_solution_history_weight.append(self.weight(current))
                
                # update current solutions
                self.curr_diameter = candidate_diameter
                self.curr_weight = candidate_weight
                self.curr_solution = candidate 

    def anneal(self):
        '''
        Annealing process 
        '''
        # as long as the temperature is greater than zero and the number of iterations is less than the maximum number of iterations
        
        self.iteration = 0
        while self.temp >= self.stopping_temp:
            while self.iteration < self.stopping_iter:
                
                # we generate a new neighbor
                first_candidate = NodeGenerator(self.original_graph, self.curr_solution).generate()   
                aux_candidate = nx.Graph.copy(first_candidate)
                
                # calculate local search
                spanTree = self.local_search(aux_candidate)
                candidate = 0

                if nx.is_connected(spanTree):
                    candidate_diameter = self.calculate_diameter(spanTree)
                    unif = random.random() # generate a uniform number between 0 and 1
                    if unif < self.acceptance_probability(candidate_diameter):
                        candidate = spanTree  #accept local search
                    else:
                        candidate = first_candidate #not accept, only cycle transition
                else:
                    candidate = first_candidate    # damage control    
                        

                # we check whether we transition or not
                self.accept(candidate)

                # if the current diameter is greater than or equal to the best diameter found
                if self.calculate_diameter(self.curr_solution) <= self.calculate_diameter(self.best_solution):
                    # if the weight of the current solution is less than or equal to the budget (feasible solution)
                    if self.weight(self.curr_solution) <= self.budget:
                        # updates the best solution
                        current = nx.Graph.copy(self.curr_solution)
                        self.best_solution = current
                        self.best_solution_history_diameter.append(self.calculate_diameter(current))
                        self.best_solution_history_weight.append(self.weight(current))
                
                # storing a history of solutions
                self.weight_list.append(self.curr_weight)
                self.diameter_list.append(self.curr_diameter)
                self.solution_history.append(self.temp)
                
                # increase the iteration
                self.iteration += 1
                
            # cooling             
            self.temp = self.temp*self.alpha 
            
            if self.alpha < 0.99:
                self.alpha = self.alpha + 0.01
                
            # update iteration
            self.iteration = 0
            
            time_total = time.time() - self.start_time
            
            if time_total >= 3600.0:
                print("Saiu pelo tempo!")
                break 
    
    def print_solution(self, start_time):
        print('Minimum weight: ', min(self.weight_list), " ", 'Improvement: ',
            round((self.initial_weight - min(self.weight_list)) / (self.initial_weight), 4) * 100, '%')
        print('Minimum diameter: ', min(self.diameter_list), " ", 'Improvement: ',
            round((self.initial_diameter - min(self.diameter_list)) / (self.initial_diameter), 4) * 100, '%')
        print('=====================================')
        print('Best Diameter', self.best_diameter)
        print('Final solution:')
        index_weight = self.best_solution_history_diameter.index(min(self.best_solution_history_diameter))
        print('Weight: ', self.best_solution_history_weight[index_weight])
        print('Diameter: ', min(self.best_solution_history_diameter))
        
        print('Iterations:', self.stopping_iter)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('=====================================')
        
    def plotLearning_diameter(self):

        fig = plt.figure(figsize=(18, 8))
        
        some_diameters = []
        for i in self.diameter_list:
            best_diam = max(self.diameter_list)
            for j in range(0, len(self.diameter_list), self.stopping_iter):
                if i < best_diam:
                    best_diam = i 
            some_diameters.append(best_diam)
        number_iterations = len(some_diameters)
        
        x_axis = np.linspace(self.initial_temp, self.temp, number_iterations)
        plt.plot(x_axis, some_diameters, color = 'blue')
    
        plt.title("Evolução do diâmetro em função da temperatura durante o algoritmo")
        
        line_init = plt.axhline(y = self.initial_diameter, color='r', linestyle='--')
        line_min = plt.axhline(y = min(self.diameter_list), color='g', linestyle='--')
        

        plt.xlim(self.initial_temp, self.temp)
        
        plt.legend([line_init, line_min], ['Initial Diameter', 'Optimized Diameter'])
        plt.ylabel('Diameter')
        plt.xlabel('Temperature')
        path = os.getcwd()
        plt.savefig(os.path.join(path, 'images', 'grafic_diameter_{}.png'.format(self.budget)), bbox_inches='tight', pad_inches=0.1)
    
    def plotLearning_best_solution_diameter(self):
        number_iterations = len(self.best_solution_history_diameter)
        
        fig = plt.figure(figsize=(18, 8))
    
        x_axis = np.linspace(self.initial_temp, self.temp, number_iterations)
        
        plt.plot(x_axis, self.best_solution_history_diameter, color = 'blue')
        plt.title("Evolução das soluções viáveis durante o algoritmo")
        
        line_init = plt.axhline(y = self.initial_diameter, color='r', linestyle='--')
        line_min = plt.axhline(y = min(self.best_solution_history_diameter), color='g', linestyle='--')

        plt.xlim(self.initial_temp, self.temp)
        
        plt.legend([line_init, line_min], ['Initial Diameter', 'Optimized Diameter'])
        plt.ylabel('Diameter')
        plt.xlabel('Temperature')
        
        path = os.getcwd()
        plt.savefig(os.path.join(path, 'images', 'grafic_best_solution_{}.png'.format(self.budget)), bbox_inches='tight', pad_inches=0.1)
        
    def plotLearning_weight(self):
        fig = plt.figure(figsize=(18, 8))

        some_weight = []
        for i in self.weight_list:
            best_weight = max(self.weight_list)
            for j in range(0, len(self.weight_list), self.stopping_iter):
                if i < best_weight:
                    best_weight = i 
            some_weight.append(best_weight)
        number_iterations = len(some_weight)
        
        self.weight_list = np.array(self.weight_list, dtype=np.float32)
        number_iterations = len(some_weight)
        x_axis = np.linspace(self.initial_temp, self.temp, number_iterations)
        plt.plot(x_axis, some_weight, color = 'blue')
        plt.title("Evolução do peso em função da temperatura durante o algoritmo")
        line_init = plt.axhline(y = self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y = min(self.weight_list), color='g', linestyle='--')
        line_budget = plt.axhline(y = self.budget, color='purple', linestyle='--', linewidth=2)
        plt.xlim(self.initial_temp, self.temp)
        plt.legend([line_init, line_min, line_budget], ['Initial Cost', 'Optimized Cost', 'Budget'])
        plt.ylabel('Cost')
        plt.xlabel('Temperature')

        path = os.getcwd()
        plt.savefig(os.path.join(path, 'images', 'grafic_weight_{}.png'.format(self.budget)), bbox_inches='tight', pad_inches=0.1)
