# Ler KM percorrido e dias alugados de um carro.
km = float(input("Digite a qtde de km percorridos: "))
dias = int(input("Digite a quantidade de dias alugado: "))
p = (dias * 60) + (km * 0.15)
print("O valor total a pagar é de R${}".format(p))