soma = 0
i= 0

while i < 5:
    nota = float(input(f"nota {1+i}:"))
    soma += nota
    i+=1 
print ("media final:", soma/5)