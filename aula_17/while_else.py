"""
While / Else
contadores e acumoladores
"""
contador = 1
acumulador = 0

while contador <= 20:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no ELSE')

