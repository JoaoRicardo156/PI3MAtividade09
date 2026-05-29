horas = int(input("Quantas horas? "))

i = 1
total = 0

while i <= horas:
    pecas = int(input("Peças: "))
    total += pecas
    i += 1

print(total)
print(total / horas)
