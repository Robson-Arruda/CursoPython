contador = 0
for n in range(10, 1, -1):
    print(contador, n)
    contador += 1
print('')
#  ou
print('***********************')
print('')
for p, n in enumerate(range(10, 1, -1)):
    print(p, n)
