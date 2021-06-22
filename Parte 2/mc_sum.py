""" 
### Questão 5

Seja $X_i$ uma sequência i.i.d. de v.a. contínuas uniformes em $[0, 1]$. 
Seja $V$ o menor número k tal que a soma das primeiras k variáveis seja maior do que 1. Ou seja, $V = min\{k | X1 +...+ X_k ≥ 1\}$.

1.   Escreva e implemente um algoritmo para gerar uma amostra de $V$.
2.   Escreva e implemente um algoritmo de Monte Carlo para estimar o valor esperado de $V$
3.   Trace um gráfico do valor estimado em função do número de amostras. Para qual valor seu estimador está convergindo?
"""

def generate_samples():
    eps = 0.000001
    k = 1
    sum_values = 0
    while True:
        X = random.uniform(0,1)
        sum_values = sum_values + X
        if sum_values >= 1 - eps:
            return k 
        else: 
            k = k + 1
            
def monte_carlo(n):
    soma_amostras = 0
    for i in range(n):
        k = generate_samples()
        soma_amostras = soma_amostras + k 

    return soma_amostras/n

"""
Trace um gráfico do valor estimado em função do número de amostras. Para qual valor seu estimador está convergindo?
"""
n_aux = 1000 # number of samples
n = list(range(1,1000))
estimate_value = monte_carlo(n_aux)

# Figure Parameters #
fig = plt.figure(figsize=(15,8))
plt.title('Distribuição de n = {} amostras e suas respectivas estimativas'.format(n_aux)) # Title
plt.ylabel('Estimativa') # y label
plt.xlabel('Número de Amostras') # x label
plt.xlim([0, n_aux]) # x limits
plt.annotate('Converge para {}'.format(estimate_value), xy=(n_aux-100, 2.8), xytext=(n_aux-200, 2.9),
            arrowprops=dict(facecolor='red', shrink=0.05),
            )  # Annotation 

# Plots
for i in n:
    plt.plot(i, monte_carlo(i), 'bo', color = 'black')
plt.axhline(y = estimate_value, c='green',linewidth = 3)

# Save and download image 
plt.show()
plt.savefig("abc.png")