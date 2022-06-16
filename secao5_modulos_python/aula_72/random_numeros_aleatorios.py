import random
import string

# Gera um número inteiro entre A e B
inteiro = random.randint(10, 20)
# Gera um número aleatório utilizando a função range()
inteiro1 = random.randrange(150, 1000, 10)
# Gera um de ponto flutuante entre A e B
flutuante = random.uniform(10, 20)
# Gera um número de ponto fluente entre 0 e 1
flutuante01 = random.random()

participantes = ['Robson', 'Thelma', 'João', 'Jean', 'Ana', 'Jandira', 'Mércia']
sorteio = random.choice(participantes)
sorteio1 = random.choices(participantes, k=2)  # Sorteando 2 nomes, retorna uma lista com 2 escolhidos
sorteio2 = random.sample(participantes, 2)  # No choices o sorteado pode se repetir, já no sample não

random.shuffle(participantes)  # Embaralha toda a ordem da lista original.

# Gera Senha Aleatória
letras = string.ascii_letters  # Letras maiusculas e minúsculas
digitos = string.digits  # numeros (digitos)
caracteres = '!@#$%&*.-_'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=12))

print(senha)

print(inteiro)
print(inteiro1)
print(flutuante)
print(flutuante01)
print(sorteio)
print(sorteio1)
print(sorteio2)
print(participantes)