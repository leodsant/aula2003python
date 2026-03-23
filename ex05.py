branco = int(input("Insira o numero total de votos brancos: "))
nulo = int(input("Insira o numero total de votos nulos: "))
valido = int(input("Insira o numero total de votos válidos: "))

total = branco + nulo + valido

print(f"o numero de votos em branco representa: {branco/total * 100:.4}%, nulos: {nulo/total * 100:.4}% e válidos: {valido/total * 100:.4}% a partir do total de votos da eleição")
