"""
Descreva uma proposta simples de função de probabilidade para gerar amostras de $X$ usando Rejection Sampling. Calcule a eficiência dessa proposta.
Usaremos g(X) = 1. Logo, f_x(X)= c*g(X) => c = max_{f_x(X)}
A eficiência é de 0.031.
"""

from scipy.stats import binom
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import random 
import requests
import string

n = 1000
p = 0.2
fig = plt.figure(figsize=(15,8))
r_values = list(range(n + 1))
distr = np.linspace(120, 280, 281)
dist = [binom.pmf(r, n, p) for r in r_values ]
maximum = binom.pmf(n*p, n, p)

inside = []
outside = []

num_amostras = 1000

cont_inside = 0
cont_outside = 0
for i in range(num_amostras):
    x = random.randint(120,280)
    u = random.uniform(0, maximum)
    if u < binom.pmf(x, n, p):
        plt.plot(x, u, 'ro', color='blue')
        cont_inside = cont_inside + 1
    else:
        cont_outside = cont_outside + 1
        plt.plot(x, u, 'ro', color= 'green')


plt.title("Número de amostras n={}".format(num_amostras))
plt.plot(r_values, dist, linewidth = 4, color = 'blue', label = 'Dentro da binomial {} pontos'.format(cont_inside))
plt.xlim([120, 280])
plt.axhline(y = maximum+0.001, c='green',linewidth = 3, label = 'Fora da binomial {} pontos'.format(cont_outside))
plt.legend(loc = 'best')


"""
Lembrando que a distribuição Binomial tem a forma de sino, centrada em sua média, proponha outra função de probabilidade para gerar amostras de X  
usando Rejection Sampling. Calcule a eficiência dessa proposta e compare com a eficiência acima. O que você pode concluir?

Usaremos a distribuição normal para estimar a binomial. Assim, X~Bin(n,p) => X~(np, sqrt(np(1-p)), onde g_X(x) é a função de densidade dessa distribuição.

f_X(x) = g_X(x)*c => c = max{f_X(x)/g_X(x)} => c = 1.0004375953661317.

Podemos concluir que essa aproximação é muito mais eficiente, uma vez que é bem próximo de 1. 
Já a outra abordagem, é pouco eficiente, como vimos no gráfico.

"""

n = 1000
p = 0.2
fig = plt.figure(figsize=(15,8))

r_values = list(range(n + 1))
distr = np.linspace(120, 280, 281)
dist = [binom.pmf(r, n, p) for r in r_values ]

inside = []
outside = []

data = np.arange(120,280,0.01)
pdf = norm.pdf(data , loc = 200, scale = math.sqrt(160))
maximum = stats.norm.pdf(200, 200, math.sqrt(160))/(binom.pmf(n*p, n, p))
cont_inside = 0
cont_outside = 0


num_amostras = 1000
for i in range(num_amostras):
    x = random.randint(120,280)
    u = random.uniform(0, maximum*(stats.norm.pdf(x, 200, math.sqrt(160))))
    if u < binom.pmf(x, n, p):
        plt.plot(x, u, 'ro', color='blue')
        cont_inside = cont_inside + 1
    else:
        cont_outside = cont_outside + 1
        plt.plot(x, u, 'ro', color= 'green')


plt.title("Número de amostras n={}".format(num_amostras))
plt.plot(r_values, dist, color = 'blue', label = 'Dentro da binomial {} pontos'.format(cont_inside))
plt.xlim([120, 280])

sb.lineplot(data, pdf, color = 'green', label = 'Fora da binomial {} pontos'.format(cont_outside))
plt.legend(loc = 'best')
print(maximum)