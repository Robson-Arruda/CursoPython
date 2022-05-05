"""
For in em Python
iterando strings com fot
Função range(start=0, stop, step=1)
"""
texto = 'Python'

# for letra in texto:
#     print(letra)

# for n, letra in enumerate(texto):
#     print(n, letra)  # Com o valor do índice

# for numero in range(2, 51, 2):  # (start, stop, step)
#     print(numero)

for n in range(100):  # encontrando múltiplos de 8
    if n % 8 == 0:
        print(n)
