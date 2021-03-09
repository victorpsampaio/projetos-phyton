#Gabriel Araújo, Vinicius Fernandes, Victor Prado e Wesciley Junio

x = 0
y = 2
z = 4

p = 0.2

while (x <= 1):
    print (round(x,2),"\t", round(y,2),"\t",round(z,2))
    x = x + 0.2
    y = y + (-2*y + 4 * 2.71 ** (-x)) * p
    z = z + ((-y * z**2) / 3) *p