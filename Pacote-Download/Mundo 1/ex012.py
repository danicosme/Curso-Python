#Faça um algoritmo que leia um preço e aplique 5% de desconto.

preco = float(input('Preço: '))
desc = preco - (preco * 5/100)

print(f'R${preco} com desconto de 5% é: {desc}')