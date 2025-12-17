while True:
    op = input("1-Somar  2-Subtrair  3-Sair: ")

    if op == "3":
        break

    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    if op == "1":
        print(a + b)
    elif op == "2":
        print(a - b)
