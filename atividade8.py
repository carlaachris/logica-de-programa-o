produto = 1
i= 0
 
while i < 10:
    num = int(input(f"digite o {i+1}º numero: "))
    produto*= num 
    i += 1
print ("o produto de todos os numeros é: ", produto)