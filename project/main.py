from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing
from simulated_temperature import SimulatedAnnealing_initial
from read_files import *
import time
import os 

def main():
    cwd = os.getcwd()+'\\instances\\'
    instance = 'states_brazil.txt'
    path = cwd+instance
    
    '''set instances parameters'''
    n, m, matrix_cost = readFiles(path, True)
    G = create_graph(n, matrix_cost)
    B = 13000
    
    print("Instance: {} with {} nodes and {} edges".format(instance, n, m))
    print("Budget: ", B)
    
    '''set the simulated annealing algorithm params'''
    temp = 100000
    stopping_temp = 0.0001
    alpha = 0.7
    stopping_iter = m-n
    
    first = SimulatedAnnealing_initial(G, temp, alpha, stopping_temp, stopping_iter, matrix_cost, B)
    temp_initial = first.anneal()
    print('Initial temperature: ', temp_initial)
    print("Maximum iteration: ", stopping_iter)
    print("Tolerance: ", stopping_temp)
    
    '''start time'''
    start_time = time.time()
    
    '''run simulated annealing'''
    sa = SimulatedAnnealing(G, temp_initial, alpha, stopping_temp, stopping_iter, matrix_cost, B, start_time)
    sa.anneal()
    
    '''show the improvement'''
    sa.print_solution(start_time)

    # '''ploting solution'''
    sa.plotLearning_diameter()
    sa.plotLearning_weight()
    sa.plotLearning_best_solution_diameter()
    
if __name__ == "__main__":
    main()




