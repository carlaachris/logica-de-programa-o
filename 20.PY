soma = cont = pares = 0
maior = menor = None

while True:
    n = int(input("Número (0 para parar): "))
    if n == 0:
        break

    soma += n
    cont += 1
    pares += n % 2 == 0

    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

print(cont, soma / cont, maior, menor, pares)
