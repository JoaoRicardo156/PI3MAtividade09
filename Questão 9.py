opcao = 0

while opcao != 3:

    print("1-Somar")
    print("2-Subtrair")
    print("3-Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        a = int(input())
        b = int(input())
        print(a + b)

    elif opcao == 2:
        a = int(input())
        b = int(input())
        print(a - b)
