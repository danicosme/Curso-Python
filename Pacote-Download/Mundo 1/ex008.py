#Escreva um programa que leia um valor em metros e converta em centímetros e milimetros.

valor = float(input('Metragem: '))

print()
print('-'*30)
print('Conversão'.center(30))
print('-'*30)
print(f'Centímetros: {valor*100} \nMilímetros: {valor*1000}')
