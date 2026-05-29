orcamento = float(input("Orçamento: "))
total = 0

while total <= orcamento:

    gasto = float(input("Gasto: "))

    if gasto < 0:
        break

    total += gasto

print(total)
print(orcamento - total)
