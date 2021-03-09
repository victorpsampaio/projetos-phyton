#Gabriel Araújo, Vinicius Fernandes, Victor Prado e Wesciley Junio

def funcao(y, x):
    return (-2*y + 4*2.71**(-x))

y = 2
x = 0
p = 0.2

k = []

for i in range (4):
    x = x + p
    k.append(funcao(y,x))
    y = 2 + k[i] * p
    print(k[i])
 
