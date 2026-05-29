idade = int(input("Digite a idade: "))

while idade < 0 or idade > 150:
    idade = int(input("Digite novamente: "))

print("Idade válida")
