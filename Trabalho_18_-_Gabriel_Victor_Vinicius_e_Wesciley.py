#Gabriel Araújo, Vinicius Fernandes, Victor Prado e Wesciley Junio
import numpy as np
import math

def f(x):
    f = (math.log(x-5,3))
    return f

def impar(j):
    func = 0
    for i in range(0,n,2):
        func=func+f(j[i])
    return func
        
def par(j):
    func = 0
    for i in range(1,n,2):
        func=func+f(j[i])
    return func

def soma(a,b,n):
    j = np.linspace(a,b,num=n)
    func = f(a)+4*impar(j)+2*par(j)+f(b)
    return func
    
a = 7
b = 17
n = 20
S = soma(a,b,n)

I = ((b-a)/(3*n))*(S)
print(I)