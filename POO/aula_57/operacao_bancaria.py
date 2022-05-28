from conta_bancaria import *

cp = ContaPoupanca(2523, 1000001, 5000)
cp.detalhes()
cp.sacar(125.25)
cp.deposito(265.99)


print('#####################')

cc = ContaCorrente(1010, 252698, 5000)
cc.detalhes()
cc.sacar(5001)
cc.sacar(300)
cc.sacar(200)
cc.sacar(199)
cc.deposito(521)
