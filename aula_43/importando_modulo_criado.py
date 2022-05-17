from calcula_preco import aumento, reducao

preco = 69.90
aumentar_preco = aumento(preco, int(input('Quantos porcento quer aumentar?\n')), formata=True)
print(aumentar_preco)

diminuir_preco = reducao(preco, int(input('Quantos porcento de desconto?\n')), formata=True)
print(diminuir_preco)
