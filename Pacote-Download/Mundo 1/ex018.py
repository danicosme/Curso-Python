#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno, tangente desse angulo

from math import sin, cos, tan, radians
angulo = float(input('Angulo: '))

print(f'Seno: {sin(radians(angulo))}.')
print(f'Cosseno: {cos(radians(angulo))}.')
print(f'Tangente: {tan(radians(angulo))}.')