import math

print('Calculando as raíses de uma função de segundo grau.')
print('Ax^2 + Bx +c')

a = int(input('Entre com valor de A: '))

if a != 0:
    b = int(input('Entre com valor de B:'))
    c= int(input('Entre com valor de C:'))
    delta = (b**2) - (4*a*c)
    print(f'o valor de Delta é :{delta}')


    if delta < 0:
        print(f'Delta é negativo.Função não possui raízes reais.')
    elif delta == 0:
        raiz = -b / 2*a
        print(f'Delta igual a zero, portanto possui apenas 1 raiz real:{raiz}')
    else:
        raizP = (-b + math.sqrt(delta)) / (2*a)
        raizN = (-b + math.sqrt(delta)) / (2*a)    
    print(f'As raízes da função {a}x^2 {b}x + {c} são {raizP} e {raizN}')
else:
    print('Se a = 0 não temos uma fução do segundo grau!')