soma_dos_pares= 0
soma_dos_impares=0
contador=0
while contador<10:
    num=int(input("digite um número:"))
    if num % 2 == 0:
        soma_dos_pares+=num
    else:
        soma_dos_impares+=num
    contador+=1
print("a soma dos números pares é",soma_dos_pares)   
print("a soma dos números impares é",soma_dos_impares) 