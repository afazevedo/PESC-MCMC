"""
    1. Construa um simulador para essa cadeia de Markov.
    
    Seja $\pi_0$ um ponto inicial qualquer. Suponha que queremos simular o que acontece no ponto $p_t$.
    1. Se vizinho for leste ou sul, então se afasta com probabilidade $p_i = \frac{1-p}{2}$
    2. Se vizinho for oeste ou norte, então se aproxima com probabilidade $p_i = \frac{p}{2}$
    3. Self-loop: $p_e = 1-\displaystyle\sum_{i \neq e} p_i$

"""

import numpy as np
import matplotlib.pyplot as plt

def simulador_latice(point, p):
    
    i = point[0]
    j = point[1]
    
    
    if point == (1,1): # Quina
        v_l = (1,2)
        v_s = (2,1)
        v_e = (1,1)
        v_n = point 
        v_o = point 
    elif point == (1, j): #Borda horizontal
        v_s = (i+1, j)
        v_l = (i, j+1)
        v_o = (i, j-1)
        v_e = (1, j)
        v_n = point
    elif point == (i, 1): #Borda lateral
        v_s = (i+1, j)
        v_n = (i-1, j)
        v_l = (i, j+1)
        v_e = (i, 1)
        v_o = point
    else:  # Meio
        v_l = (i, j+1)
        v_o = (i, j-1)
        v_s = (i+1, j)
        v_n = (i-1, j)
        v_e = point

    neighbors = [v_l, v_s, v_o, v_n, v_e]
    prob_v = []
    neighbors_dispel = [v_l, v_s] #Vizinhos que se dispersão
    neighbors_approximate = [v_o, v_n] # Vizinhos que se aproximam
    self_loop = v_e #self-loop
    soma = 0

    for v in neighbors_dispel:
        if v != point:
            prob_v.append(p/2)
            soma = soma + p/2
        else:
            prob_v.append(0)
        

    for v in neighbors_approximate:
        if v != point:
            prob_v.append((1-p)/2)
            soma = soma + (1-p)/2 
        else: 
            prob_v.append(0)
        
    if soma < 1: 
        prob_v.append(1-soma) # Coloca o resto da probabilidade no self-loop
    else:
        prob_v.append(0)

    ind = np.random.choice(list(range(5)), 1, p = prob_v)[0] # Escolhe um vizinho aleatoriamente
    neighbor_chosen = neighbors[ind]
    return neighbor_chosen
    