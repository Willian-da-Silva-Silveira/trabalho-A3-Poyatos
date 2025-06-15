#Aqui estou importando a função exit para finalizar o programa, caso precise
from sys import exit

#Essa área é dedicada para organizar os menus e demais informações para chamar futuramente.
#Me fazendo digitar menos
listaUnidadeMedida = '''
01 - Metros
02 - Centímetros
03 - Decímetros
04 - Milímetros
05 - Litros
06 - Mililitros
'''

menu = '''
01 - Área de quadrado
02 - Área de retângulo
03 - Área de triângulo
04 - Área de Trapézio
05 - Área do círculo
06 - Volume de cubo
07 - Volume de cilindro
08 - Volume de prisma
09 - Volume de trapézio
'''


class metros:
    unidade = "metros"
    simboloArea = "m²"
    simboloVolume = "m³"

class centimetros:
    unidade = "centímetros"
    simboloArea = "cm²"
    simboloVolume = "cm³"

class decimetros:
    unidade = "decímetros"
    simboloArea = "dm²"
    simboloVolume = "dm³"

class milimetros:
    unidade = "mm"
    simboloArea = "mm²"
    simboloVolume = "mm³"

class litros:
    unidade = "litros"
    simboloVolume = "lt"

class mililitros:
    unidade = "mililitros"
    simboloVolume = "mi"

#Aqui ficam os textos que são padrão
escolherUnidade = "Digite o nome da unidade que você deseja trabalhar.\n{}"
escolherFormula = "Digite o número do item que você quer calcular.\n{}"

#Essa área é dedicada para o usuário definir qual conta deseja fazer.
unidadeEscolhida = str(input(escolherUnidade.format(listaUnidadeMedida)))

unidadeEscolhida.lower()

if unidadeEscolhida == "metros":
    unidadeEscolhida = metros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

elif unidadeEscolhida == "centímetros" or unidadeEscolhida == "centimetros":
    unidadeEscolhida = centimetros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

elif unidadeEscolhida == "decímetros" or unidadeEscolhida == "decimetros":
    unidadeEscolhida = decimetros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

elif unidadeEscolhida == "milímetros" or unidadeEscolhida == "milimetros":
    unidadeEscolhida = milimetros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

elif unidadeEscolhida == "litros":
    unidadeEscolhida = litros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

elif unidadeEscolhida == "mililitros":
    unidadeEscolhida = mililitros()
    formulaEscolhida = int(input(escolherFormula.format(menu)))

else:
    print("Essa opção não existe !\nPor favor, reinicie o programa.")
    exit()


#Essa área é dedicada para criar as classes de cada fórmula.
class areaQuadrado:
    formula = "A=a*b"
    def calcular(self):
        valorDe_a = float(input("Qual é o valor de a em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        print("A área é de {:.2f}{}".format(valorDe_a * valorDe_b, unidadeEscolhida.simboloArea))

class areaRetangulo:
    formula = "A=a*b"
    def calcular(self):
        valorDe_a = float(input("Qual é o valor de a em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        print("A área é de {:.2f}{}".format(valorDe_a * valorDe_b, unidadeEscolhida.simboloArea))

class areaTriangulo:
    formula = "A=a*b/2"
    def calcular(self):
        valorDe_a = float(input("Qual é o valor de a em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        print("A área é de {:.2f}{}".format(valorDe_a * valorDe_b / 2, unidadeEscolhida.simboloArea))

class areaTrapezio:
    formula = "A=(B+b)*h/2"
    def calcular(self):
        valorDe_B = float(input("Qual é o valor de B em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_h = float(input("Qual é o valor de h em {} ?\n".format(unidadeEscolhida.unidade)))
        print("A área é de {:.2f}{}".format((valorDe_B + valorDe_b) * valorDe_h / 2,
                                            unidadeEscolhida.simboloArea))

class areaCirculo:
    formula = "A=r²*PI/2"
    def calcular(self):
        valorDe_r = float(input("Qual é o valor de r em {} ?\n".format(unidadeEscolhida.unidade)))
        print("A área é de {:.2f}{}".format((valorDe_r ** 2) * 3.1415 / 2, unidadeEscolhida.simboloArea))

class volumeCubo:
    formula = "V=(a*b)*h"
    def calcular(self):
        valorDe_a = float(input("Qual é o valor de a em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_h = float(input("Qual é o valor de h em {} ?\n".format(unidadeEscolhida.unidade)))
        print("O volume é de {:.2f}{}".format((valorDe_a * valorDe_b) * valorDe_h,
                                              unidadeEscolhida.simboloVolume))

class volumeCilindro:
    formula = "V=(r²*PI/2)*h"
    def calcular(self):
        valorDe_r = float(input("Qual é o valor de r em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_h = float(input("Qual é o valor de h em {} ?\n".format(unidadeEscolhida.unidade)))
        print("O volume é de {:.2f}{}".format(((valorDe_r ** 2) * 3.1415 / 2) * valorDe_h,
                                              unidadeEscolhida.simboloVolume))

class volumePrisma:
    formula = "V=(1/2)*b*h*i"
    def calcular(self):
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_h = float(input("Qual é o valor de h em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_i = float(input("Qual é o valor de i em {} ?\n".format(unidadeEscolhida.unidade)))
        print("O volume é de {:.2f}{}".format((1 / 2) * valorDe_b * valorDe_h * valorDe_i,
                                              unidadeEscolhida.simboloVolume))

class volumeTrapezio:
    formula = "V=((1/2)*h*(B+b))*w"
    def calcular(self):
        valorDe_h = float(input("Qual é o valor de h em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_B = float(input("Qual é o valor de B em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_b = float(input("Qual é o valor de b em {} ?\n".format(unidadeEscolhida.unidade)))
        valorDe_w = float(input("Qual é o valor de w em {} ?\n".format(unidadeEscolhida.unidade)))
        print("O volume é de {:.2f}{}".format((1 / 2) * valorDe_h * (valorDe_B + valorDe_b) * valorDe_w,
                                              unidadeEscolhida.simboloVolume))

#Essa área é dedicada para executar os calculos, de acordo com o retorno do usuário
if formulaEscolhida == 1:
    print("A fórmula para descobrir a área do quadrado é {}".format(areaQuadrado.formula))
    areaQuadrado.calcular(areaQuadrado)

elif formulaEscolhida == 2:
    print("A fórmula para descobrir a área do retângulo é {}".format(areaRetangulo.formula))
    areaRetangulo.calcular(areaRetangulo)

elif formulaEscolhida == 3:
    print("A fórmula para descobrir a área do triângulo é {}".format(areaTriangulo.formula))
    areaTriangulo.calcular(areaTriangulo)

elif formulaEscolhida == 4:
    print("A fórmula para descobrir a área do trapézio é {}".format(areaTrapezio.formula))
    areaTrapezio.calcular(areaTrapezio)

elif formulaEscolhida == 5:
    print("A fórmula para descobrir a área do círculo é {}".format(areaCirculo.formula))
    areaCirculo.calcular(areaCirculo)

elif formulaEscolhida == 6:
    print("A fórmula para descobrir o volume do cubo é {}".format(volumeCubo.formula))
    volumeCubo.calcular(volumeCubo)

elif formulaEscolhida == 7:
    print("A fórmula para descobrir o volume do cilindro é {}".format(volumeCilindro.formula))
    volumeCilindro.calcular(volumeCilindro)

elif formulaEscolhida == 8:
    print("A fórmula para descobrir o volume de um prisma é {}".format(volumePrisma.formula))
    volumePrisma.calcular(volumePrisma)

elif formulaEscolhida == 9:
    print("A fórmula para descobrir o volume de um trapezio é {}".format(volumeTrapezio.formula))
    volumeTrapezio.calcular(volumeTrapezio)

else:
    print("Essa função não existe!\nPor favor, reinicie o programa.")
    exit()