custoFabrica = float(input("Insira o custo de fábrica do carro: "))
custoFabrica+= custoFabrica * 0.45
distribuidor = custoFabrica * 0.28

print(f"o custo final do consumidor é de: R${custoFabrica + distribuidor:.12}")