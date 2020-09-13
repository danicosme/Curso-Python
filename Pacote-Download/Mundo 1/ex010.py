#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 
#Considere: 1 dólar = 3,27 reais

carteira = float(input('Dinheiro total: R$'))

print(f'Em dolár você tem R${carteira/3.27:.2f}')