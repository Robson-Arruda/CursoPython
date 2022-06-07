from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# terça, 07 de Junho de 2022

setlocale(LC_ALL, 'pt_BR.utf-8')
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao)
print(formatacao2)

print(mdays[mes_atual])
