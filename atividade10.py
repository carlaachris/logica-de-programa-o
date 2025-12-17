maior = None
menor = None

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))

    if maior is None or num > maior:
        maior = num

    if menor is None or num < menor:
        menor = num

print("\nMaior número digitado:", maior)
print("Menor número digitado:", menor)