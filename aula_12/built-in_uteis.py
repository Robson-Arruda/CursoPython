# isnumeric, isdigit, isdecimal

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# entendo o retorno de acordo com o dados enviados

print(num1.isnumeric())
print(num2.isnumeric())
print(num1.isdigit())
print(num2.isdigit())
print(num1.isdecimal())
print(num2.isdecimal())

# se houver qq caracter que não seja numero (. -) o retorno é sempre false

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Digite somente números inteiros')


