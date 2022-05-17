# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log:', error)
#         raise  # Tratei a exceção e relancei o erro no sistema. Exemplo criar um log do erro
#
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as erro:
#     print(erro)

# def divide(n1, n2):
#     if n2 == 0:
#         raise ValueError("N2 não pode ser 0.")
#     return n1 / n2
#
#
# try:
#     print(divide(2, 0))
# except ValueError as error:
#     print('Não é possível dividir um numero por 0')
#     print('log:', error)

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass  # Retorna None


numero = converte_numero(input('Digite um Número: '))

if numero is None:
    print('Digite somente números')

else:
    print(numero * 5)
