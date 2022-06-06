# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta
#                  a  m  d  h   m   s   ano, mes, dia, hora, minuto, segundo
data = datetime(2022, 5, 6, 16, 48, 59)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(f'#####################\n')

# RECEBENDO UMA DATA EM STR
data1 = datetime.strptime('06/05/2022', '%d/%m/%Y')
print(data1)
print(f'#####################\n')

print(data.timestamp())
data2 = datetime.fromtimestamp(1651806000.0)
print(data2)
print(f'#####################\n')

data = data + timedelta(days=5, hours=2, seconds=3)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data3 = datetime.strptime('25/04/1989 08:27:53', '%d/%m/%Y %H:%M:%S')
print(data3.strftime('%d/%m/%Y %H:%M:%S'))
print(f'#####################\n')

data4 = datetime.strptime('06/05/2022 17:18:59', '%d/%m/%Y %H:%M:%S')
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
print(f'#####################\n')

dif = data4 - data3
print(dif.days)