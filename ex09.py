dias = int(input("insira o número de dias trabalhados: "))
total = dias * 180
imposto = total * 0.08
print(f"o valor a ser recebido após o desconto do imposto de renda é: R${total - imposto}")