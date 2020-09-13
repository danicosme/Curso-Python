#Faça um programa que leia altura e largura de uma parede em metros e calcule sua área e a quantidade de tinta
# necessária para pintá-la sabendo que a cada litro de tinta, é pintado uma área de 2m².

altura = float(input('Altura: '))
largura = float(input('Largura: '))

a = (altura * largura) 

print(f'Em uma parade de área {a} m², será necessário {a/2}L de tinta.')