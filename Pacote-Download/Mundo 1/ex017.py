#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot
o = float(input('Cateto oposto: '))
a = float(input('Cateto adjacente: '))

print(f'O compromimento da hipotenusa é: {hypot(o,a):.2f} cm.')


