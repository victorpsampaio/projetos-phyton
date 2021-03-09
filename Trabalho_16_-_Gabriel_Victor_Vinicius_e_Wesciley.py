#Gabriel AraÃºjo, Victor Prado, Vinicius Fernandes, Wesciley Junio

import numpy as np

x = np.array([10, 11, 12, 13, 14, 15]) #TABELA
fx = np.array([1400, 1900, 2500, 3250, 4200, 5400])

def pos(k) : #POSIÃÃO
    cont=0
    for i in x:
        if i == k:
            return cont
        else: cont = cont + 1
   
def segunda(a,b):  #SEGUNDA DIVISÃO
    l1 = fx[a]-fx[b]
    l2 = x[a]-x[b]
    return (l1/l2)

def terceira(a,b,c): #TERCEIRA DIVISÃO
    l1 = segunda(a,b) - segunda(b,c)
    l2 = x[a]-x[c]
    return (l1/l2)

def quarta(a,b,c,d): #QUARTA DIVISÃO
    l1 = terceira(a,b,c) - terceira(b,c,d)
    l2 = x[a]-x[d]
    return (l1/l2)

def quinta(a,b,c,d,e): #QUINTA DIVISÃO
    l1 = quarta(a,b,c,d) - quarta(b,c,d,e)
    l2 = x[a]-x[e]
    return (l1/l2)
    
def sexta(a,b,c,d,e,f): #SEXTA DIVISÃO
    l1 = quinta(a,b,c,d,e) - quinta(b,c,d,e,f)
    l2 = x[a]-x[f]
    return (l1/l2)
    
def f3(k): #POLINOMIO INTERPOLADOR DE NEWTON DE 3a ORDEM
    b1 = fx[0]
    b2 = segunda(1,0)
    b3 = terceira(2,1,0)
    b4 = quarta(3,2,1,0)
    
    f3 = b1 + (b2*(k-x[0])) + (b3*(k-x[0])*(k-x[1])) + (b4*(k-x[0])*(k-x[1])*(k-x[2]))
    return f3

def coeficientes(): #CÃLCULO DOS COEFICIENTES
    b1 = fx[0]
    b2 = segunda(1,0)
    b3 = terceira(2,1,0)
    b4 = quarta(3,2,1,0)
    print("\nB1= " + str(b1) + "\nB2=" + str(b2) +"\nB3=" + str(b3) + "\nB4=" + str(b4))
   
#LETRA A
print("\n")
print("Coeficientes: \n")
coeficientes()


a, b = 0,130

# Insira o valor do incremento:
Dx = 0.2

# Inicia as variáveis
x1, x2 = a, a+Dx
F1, F2 = f3(x1), f3(x2)

# Executa o laço enquanto F1*F2 for maior que zero, ou, quando x1 for maior e igual a b.
while F1*F2 > 0.0:
    if x1 >=b:
        
        break
    x1, F1 = x2, F2
    x2 = x1 + Dx
    F2 = f3(x2)
else:
    # Imprime os limites do pequeno intervalo de comprimento Dx que contém pelo menos
    # uma raíz da função
    print("\n")
    print("Valor de x está entre: ")
    print(x1, x2)
    
print("\n")


