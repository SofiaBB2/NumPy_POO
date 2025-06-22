import numpy as np

class Calculadora():
    def __init__(self, nome):
        self.nome = nome

    def __str__(self) -> str:
        apresentar = f"Olá! Meu nome é {self.nome} e estou aqui para te ajudar a calcular algo. Por onde quer começar?"
        return apresentar

    def potencia(self, base, exp) -> float:
        r = np.power(base, exp)
        return r

    def cos(self, angulo) -> float:
        r = np.cos(angulo)
        return r
    def sen(self, angulo) -> float:
        r = np.sin(angulo)
        return r
    def tg(self, angulo) -> float:
        r = np.tan(angulo)
        return r

    def aprox(self, n) -> int:
        r = np.round(n)
        return r
    def chao(self, n) -> int:
        r = np.floor(n)
        return r
    def teto(self, n) -> int:
        r = np.ceil(n)
        return r

    def cte(self) -> str:
        r = f"Número de Euler (e): {np.e} \n Valor aproximado de pi (π): {np.pi}"
        return r

    def converterRad(self, rad) -> float:
        r = np.rad2deg(rad)
        return r
    def converterGraus(self, graus) -> float:
        r = np.deg2rad(graus)
        return r
    
    def menu(self) -> int:
        print("\n-----------------MENU------------------\n")
        print("0 - sair do programa;")
        print("1 - potência;")
        print("2 - cosseno;")
        print("3 - seno;")
        print("4 - tangente;")
        print("5 - aproximar;")
        print("6 - arrendondar para baixo;")
        print("7 - arredondar para cima;")
        print("8 - mostrar constantes;")
        print("9 - converter de radianos para graus;")
        print("10 - converter de graus para radianos.")
        op = int(input("\nQual é a opção escolhida?\n" ))

        return op
    
    def chamarMetodos(self, op):
        if(op == 1):
            base = float(input("Informe a base: "))
            exp = float(input("Informe o expoente: "))
            resp = self.potencia(base, exp)

        elif(op == 2):
            angulo = float(input("Informe o ângulo (em radianos): "))
            resp = self.cos(angulo)

        elif(op == 3):
            angulo = float(input("Informe o ângulo (em radianos): "))
            resp = self.sen(angulo)

        elif(op == 4):
            angulo = float(input("Informe o ângulo (em radianos): "))
            resp = self.tg(angulo)

        elif(op == 5):
            num = float(input("Informe o número que será aproximado: "))
            resp = self.aprox(num)

        elif(op == 6):
            num = float(input("Informe o número que será arredondado para baixo: "))
            resp = self.chao(num)

        elif(op == 7):
            num = float(input("Informe o número que será arredondado para cima: "))
            resp = self.teto(num)

        elif(op == 8):
            resp = self.cte()
            
        elif(op == 9):
            rad = float(input("Informe a medida em radianos (π): "))
            resp = self.converterRad(rad)

        elif(op == 10):
            graus = float(input("Informe a medida em graus (°)"))
            resp = self.converterGraus(graus)
        else:
            resp = "Opção inválida!"
        
        return resp