from models import *

nome = input("Defina um nome para sua nova calculadora científica: ")

calc = Calculadora(nome)

print(calc)

op = -1

while(op != 0):
    op = calc.menu()
    if(op == 0):
        print("Fim!")
        break
    else:
        resp = calc.chamarMetodos(op)
        print(resp)
        