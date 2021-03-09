"""
Alunos: Gabriel Jordão
        Victor Sampaio
        Vinícius Fernandes
        Wesciley Junio
"""
import numpy as np
import math

def f(x):
    f =  math.log(x-5,3)
    return f


def soma(a,b,n):
    fun=0
    j = np.linspace(a,b,num=n)
    i=0
    for i  in range(1,n):
        fun = fun +f(j[i])
    fun = 2*fun
    fun =fun+f(a)+f(b)
    return fun
    
a = 7
b = 17
# quanto maior o n mais aproximado da integração real dá
n = 10
S = soma(a,b,n)
I = ((b-a)/(2*n))*(S)
print(I)