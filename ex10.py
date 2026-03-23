comprimento = float(input("insira o comprimento da cozinha: "))
largura = float(input("insira a largura da cozinha: "))
altura = float(input("insira a altura da cozinha: "))
lado1 = comprimento * altura
lado2 = largura * altura
paredesTotais = lado1 * 2 + lado2 * 2
print(f"a quantidade de caixas necessárias para preencher todas as paredes da cozinha é: {paredesTotais / 1.5} caixas")