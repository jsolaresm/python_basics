from ast import TypeVarTuple


x = 1
y = 2.9
z = 5j

print(type(x),type(y),type(z))

positivo = 1
negativo = -1
decimal = -1.1
complejo = -5j
imaginario = 5+5j

imaginario = -5- 5j

print(type(positivo),type(negativo),type(decimal),type(complejo))

print(positivo,negativo,decimal,complejo)


xf = float(x)
print(type(xf))
print(xf)

ye = int(y)
print(type(ye))
print(ye)


entero = 55
flotante = 5.5
enterocomplejo = (complex(entero))
print(type(enterocomplejo))
floatcomplejo = (complex(flotante))
print(type(floatcomplejo))


import random

print(random.randrange(1,10)) #numero aleatorio entre 1 y 9

 