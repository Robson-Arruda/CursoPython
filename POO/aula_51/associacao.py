from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Robson')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
