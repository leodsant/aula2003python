segundos = int(input("insira um valor inteiro em segundos: "))
minutos = segundos / 60
horas = minutos / 60
segundosResto = segundos % 60

print(f"{segundos} correspondem a {horas:.5} horas, {minutos:.5} minutos e {segundosResto} segundos")