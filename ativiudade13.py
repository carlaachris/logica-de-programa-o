n= int(input("digite um numero"))

if n <= 1:
    print("não é primo")
else:
    divisor = 2
    primo= True

    while divisor < n:
        if n % divisor ==0:
            primo = False 
            break
        divisor += 1

print ("é primo. " if primo else "não é primo.")