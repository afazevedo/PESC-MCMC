""" 
2. Determine numericamente o vão espectral da cadeia de Markov para cada valor de $p$
"""
import numpy as np
from scipy import linalg as LA

def spectral_gap(matrix):
    e_vals, e_vecs = LA.eig(matrix) # Autovalores e Autovetores 
    abs_evals = np.absolute(e_vals) # Módulo
    e_vals_ordenados = sorted(abs_evals) # Ordenando de forma crescente
    lambda_2 = e_vals_ordenados[-2] # Pega o segundo auto valor 

    return (1-lambda_2)