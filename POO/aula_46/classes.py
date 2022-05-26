from pessoa import Pessoa

p1 = Pessoa(input('Qual seu nome? \n'), 33)  # Teste fora da aula
p2 = Pessoa('Thelma', 39)

p1.comer(input(f'{p1.nome} o que você gosta de comer? \n'))  # Teste fora da aula
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('maçã')
p1.parar_falar()
p1.comer('maçã')
p1.parar_comer()

p1.falar('TI')
p2.falar('Futebol')

print(p1.get_ano_nascimento())