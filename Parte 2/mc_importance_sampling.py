import numpy as np
import math
import random
from matplotlib import pyplot as plt

def get_rand_number(min_value, max_value):
    """
    This function gets a random number from a uniform distribution between
    the two input values [min_value, max_value] inclusively
    """
    range = max_value - min_value
    choice = random.uniform(0,1)
    return min_value + range*choice

def g(x):
    """
    This is the main function we want to integrate over.
    """
    return np.exp(-x**2)

def monte_carlo(num_samples):
    """
    This function performs the Monte Carlo for our
    specific function g(x).
    """
    
    sum_of_samples = 0
    for i in range(num_samples):
        x = get_rand_number(0, 10)
        sum_of_samples += g(x)
    
    return 10 * float(sum_of_samples/num_samples) 

def h(x):
    """
    This is the auxiliary function we are using.
    """
    A = (np.exp(10))/(np.exp(10)-1)
    return A*(np.exp(-x))

def inverse_H(u):
    """
    This function calculates H^{-1}(u)
    """
    A = (np.exp(10))/(np.exp(10)-1)
    return -np.log(1-u/A)


def importance_sampling(num_samples):
    """
    This function performs the Monte Carlo with 
    importance sampling.
    """

    running_total = 0
    for i in range(num_samples):
        u = get_rand_number(0,1)
        running_total += g(inverse_H(u))/h(inverse_H(u))
    approximation = float(running_total/num_samples)
    return approximation

"""
    Parameters
"""
n = 1000000
I = 0.88622
eixoX = [1, 10, 100, 1000, 10000, 100000, 1000000]
estim_mc = []
estim_is = []


"""
    Figure Parameters: Estimatives versus nº of Samples
"""

fig = plt.figure(figsize=(18,8))

plt.subplot(1, 2, 1)
plt.ylabel('Estimativa') # y label
plt.xlabel('Número de Amostras') # x label
plt.xscale('log')
plt.xlim([1, n])

for i in eixoX:  
    estim_mc.append(monte_carlo(n))
    estim_is.append(importance_sampling(n))

plt.plot(eixoX, estim_mc, color = 'black', label = 'Monte Carlo')
plt.plot(eixoX, estim_is, color = 'red', label = 'Importance Sample')
plt.axhline(y = 0.88622, c='green',linewidth = 3, label = 'Valor numérico da Integral')


"""
    Figure Parameters: Relative error versus nº of Samples
"""

estim_error_mc = []
estim_error_is = []

plt.subplot(1, 2, 2)
plt.ylabel('Estimativa de Erros Relativos') # y label
plt.xlabel('Número de Amostras') # x label
plt.xscale('log')
plt.xlim([1, n])

for i in eixoX:  
    estim_error_mc.append((abs(monte_carlo(n)-I))/I)
    estim_error_is.append((abs(importance_sampling(n)-I))/I)


plt.plot(eixoX, estim_error_mc, color = 'black', label = 'Monte Carlo')
plt.plot(eixoX, estim_error_is, color = 'red', label = 'Importance Sample')
plt.legend()
fig.suptitle('Distribuição de n = {} amostras'.format(n))
plt.show()