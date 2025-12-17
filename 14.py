import random

numero_secreto = random.randint(1, 20)

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 20): "))

    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")

print("Parabéns! Você acertou!")
