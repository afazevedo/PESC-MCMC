import networkx as nx
from initial_solution import *
import numpy as np 
import math
import random
from nodes_generator import NodeGenerator
import matplotlib.pyplot as plt
import time
import os
class SimulatedAnnealing_initial:
    def __init__(self, original_graph, initial_temp, alpha, stopping_temp, stopping_iter, matrix_cost, B):
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
        '''
        
        # set simulated annealing parameters
        self.temp = initial_temp # set temperature to initial temperature
        self.initial_temp = initial_temp
        self.alpha = alpha 
        self.stopping_temp = stopping_temp
        self.stopping_iter = stopping_iter
        
        # set initial parameters
        self.iteration = 0
        self.original_graph = original_graph
        self.dist_matrix = matrix_cost
        self.budget = B
        self.curr_solution = generate_random_tree(self.original_graph)
        
        # set initial weight parameters
        self.curr_weight = self.weight(self.curr_solution)
        aux_weight = self.curr_weight
        self.initial_weight = aux_weight
        self.min_weight = aux_weight

        # set initial diameter parameters
        self.curr_diameter = self.calculate_diameter(self.curr_solution)
        aux_diameter = self.curr_diameter
        self.initial_diameter = aux_diameter
        self.min_diameter = aux_diameter

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

    def accept(self, candidate):
        '''
        Accept with probability 1 if candidate solution is better than
        current solution, else accept with probability equal to the
        acceptance_probability()
        '''
        accepting = False
        
        # calculate the diameter and weight of the neighbor
        candidate_diameter = self.calculate_diameter(candidate)
        candidate_weight = self.weight(candidate)
            
        # if the diameter of the neighbor is smaller or equal but with a smaller weight, we accept    
        if candidate_diameter < self.curr_diameter or (candidate_diameter == self.curr_diameter and candidate_weight < self.curr_weight):
            # update current solutions
            self.curr_diameter = candidate_diameter
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
        else:
            # if not, we will accept according to boltzmann distribution
            unif = random.random() # generate a uniform number between 0 and 1
            if unif < self.acceptance_probability(candidate_diameter):
                accepting = True
                # update current solutions
                self.curr_diameter = candidate_diameter
                self.curr_weight = candidate_weight
                self.curr_solution = candidate
        return accepting
    
    def anneal(self):
        '''
        Annealing process 
        '''
        # as long as the temperature is greater than zero and the number of iterations is less than the maximum number of iterations
        
        self.iteration = 0
        while self.temp >= self.stopping_temp:
            improve = False 
            count = 0
            while self.iteration < self.stopping_iter:
                
                # we generate a new neighbor
                candidate = NodeGenerator(self.original_graph, self.curr_solution).generate()
                
                # we check whether we transition or not
                accepting = self.accept(candidate)
                if accepting:
                    count = count + 1
                
                
                # increase the iteration
                self.iteration += 1
                

            if count/(self.stopping_iter) >= 0.7:
                return self.temp
                break
            else:
                self.temp = self.temp*1.2
            
            # update iteration
            self.iteration = 0
 
