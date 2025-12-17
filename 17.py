soma = cont = 0

idade = int(input("Idade (0 para parar): "))
while idade != 0:
    soma += idade
    cont += 1
    idade = int(input("Idade (0 para parar): "))

print(soma / cont)
