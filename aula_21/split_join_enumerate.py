"""
Split, Join, Enumerate
* split - Dividir uma str
* join - Juntar uma lista #str
* enumerate - Enumerar elementos de uma lista # iteráveis
"""

# split
print('>>>> split <<<<')
string = "O Brasil é o país do futebol, o Brasil é penta"
lista = string.split(' ')
print(lista)
# Divide uma lista com o parâmetro passado entre "()"
# Caso o valor passado nos () fosse "," a lista teria um novo indice a ca "," encontrada na frase
print('')
# join
print('>>>> join <<<<')
string_1 = 'O brasil é penta'
lista_1 = string_1.split()  # separa por default no 'espaço' entre palavras
string_2 = ' '.join(lista_1)
print(lista_1)
print(string_2)
# join faz exatamento o oposto ao split, transfoma lista em string
# acima transformei uma string em lista e depois o reverso utilizando outra variável
print('')
# enumerate
print('>>>> enumerate <<<<')
for indice, valor in enumerate(lista_1):
    print(indice, valor)
# enumerate simplesmente enumera indicoes de uma lista
