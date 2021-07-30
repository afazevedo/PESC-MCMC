# -*- coding: utf-8 -*-
"""
# =============================================================================
Author: Amanda Azevedo
Python Version: 3.9.5
Email: afazevedo29@gmail.com
Course: Algoritmos de Monte Carlo e Cadeias de Markov
Date: 26/05/2020
# =============================================================================
"""

"""
#----------------------------------------------------------------------------------------------------------#
                                Questão 3
#----------------------------------------------------------------------------------------------------------#
    Considere um processo estocástico que inicia no estado $1$ e a cada instante 
    de tempo incrementa o valor do estado em uma unidade com probabilidade $p$ 
    ou retorna ao estado inicial com probabilidade $1-p$. 
    No estado $n$ o processo não cresce mais, e se mantém neste estado com probabilidade $p$. 
    Assuma que $n=1$ e que $p \in \{0.25, 0.5, 0.75\}$.
#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
"""

import numpy as np
from scipy import linalg as LA

from read_matrix import *
from spectral_gap import *
from stationary_distribution import *
from mixing_time import *

eps = 0.000001 #10^-6
delta = []
time_inf = []
time_sup = []
min_pi = []

for p in [0.25, 0.5, 0.75]:
    T = read_matrix(p)
    delta_aux = spectral_gap(T)
    stationary, min_pi_aux = stationary_distribution(p)
    time_inf_aux, time_sup_aux = mixing_time(delta_aux, eps, min_pi_aux)
    delta.append(delta_aux)
    min_pi.append(min_pi_aux)
    time_inf.append(time_inf_aux)
    time_sup.append(time_sup_aux)
    

print("Vão espectral: ",delta, "\n", "Menor valor de pi: ", min_pi, "\n", "Limite inferior para o tempo de mistura: ", time_inf, "\n", "Limite superior para o tempo de mistura: ", time_sup)