action = int(input("Digite o número do item da a fórmula que você quer calcular.\n01 - Área do de um quadrado\n"
                   "02 - Área de um retângulo\n03 - Área do circulo\n04 - Área de um triângulo\n05 - Área do trapézio\n"
                   "06 - Volume de um cubo\n07 - Volume de um cilíndro\n08 - Volume de um prisma\n"
                   "09 - Volume de um trapézio\n"))

decTy = int(input("Digite o nome da decimal você quer trabalhar ?\n01 - Metros\n02 - Centímetros\n03 - Decímetros\n"
                  "04 - Milimetros\n"))

if decTy == 1:
    decTy = "Metros"
    decSq = "m²"
    decVol = "m³"

if decTy == 2:
    decTy = "Centímetros"
    decSq = "cm²"
    decVol = "cm³"

if decTy == 3:
    decTy = "Decímetros"
    decSq = "dec²"
    decVol = "dec³"

if decTy == 4:
    decTy = "Milímetros"
    decSq = "mm²"
    decVol = "mm³"

if action == 1:
    print("A fórmula para descobrir a área de um quadrado é A=a*b\n")
    a = float(input("Qual é o valor de 'a' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    sqAr = a*b
    print("A área desse quadrado é de {:.2f} {}".format(sqAr, decSq))

if action == 2:
    print("A fórmula para descobrir a área de um retãngulo é A=a*b\n")
    a = float(input("Qual é o valor de 'a' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    recAr = a*b
    print("A área desse retângulo é de {:.2f} {}".format(recAr, decSq))

if action == 3:
    print("A fórmula para descobrir a área de um circulo é A=r²*PI/2")
    r = float(input("Qual é o raio desse circulo em {} ?\n".format(decTy)))
    cirAr = (r**2)*3.147/2
    print("A área desse circulo é de {:.2f} {}".format(cirAr, decSq))

if action == 4:
    print("A fórmula para descobrir a área de um triângulo é A=a*b/2")
    a = float(input("Qual é o valor de 'a' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    triAr = a*b/2
    print("A área desse triângulo é de {:.2f} {}".format(triAr, decSq))

if action == 5:
    print("A fórmula para descobrir a área de um trapézio é A=(B+b)*h/2")
    B = float(input("Qual é o valor de 'B' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    h = float(input("Qual é o valor de 'h' em {} ?\n".format(decTy)))
    trapAr = (B+b)*h/2
    print("A área desse trapézio pe de {:.2f} {}".format(trapAr, decSq))

if action == 6:
    print("A fórmula para descobrir o volume de um cubo é V=(a*b)*h")
    a = float(input("Qual é o valor de 'a' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    h = float(input("Qual é o valor de 'h' em {} ?\n".format(decTy)))
    cubVol = (a*b)*h
    print("O volume desse cubo é de {:.2f} {}".format(cubVol, decVol))

if action == 7:
    print("A fórmula para descobrir o volume de um cilíndro é V=(r²*PI/2)*h")
    r = float(input("Qual é o valor de 'r' (r é o raio, ok !) em {} ?\n".format(decTy)))
    h = float(input("Qual é o valor de 'h' em {} ?\n".format(decTy)))
    cilVol = ((r**2)*3.147/2)*h
    print("O volume desse cilíndro é de {:.2f} {}".format(cilVol, decVol))

if action == 8:
    print("A fórmula para descobrir o volume de um prisma é V=(1/2)*b*h*i\n")
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    h = float(input("Qual é o valor de 'h' em {} ?\n".format(decTy)))
    i = float(input("Qual é o valor de 'i' em {} ?\n".format(decTy)))
    triVol = (1/2)*b*h*i
    print("O volume desse prísma é de {:.2f} {}".format(triVol, decVol))

if action == 9:
    print("A fórmula para descobrir o volume de um trapézio é V=((1/2)*h*(B+b))*w")
    h = float(input("Qual é o valor de 'h' em {} ?\n".format(decTy)))
    B = float(input("Qual é o valor de 'B' em {} ?\n".format(decTy)))
    b = float(input("Qual é o valor de 'b' em {} ?\n".format(decTy)))
    w = float(input("Qual é o valor de 'w' em {} ?\n".format(decTy)))
    trapVol = ((1/2)*h*(B+b))*w
    print("O volume desse trapézio é de {:.2f} {}".format(trapVol, decVol))