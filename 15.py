soma = 0

while True:
    numero = int(input("Digite um número (negativo para parar): "))

    if numero < 0:
        break  # Encerra o loop quando for negativo

    soma += numero  # Soma apenas números positivos

print("A soma dos números positivos é:", soma)
