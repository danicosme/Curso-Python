#Faça um programa que leia de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
# Ex: digite 1834, unidade: 4, dezena: 3, centena: 8, milhar: 1

num = int(input('Número: '))

u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10

print(f'\nUnidade: {u} \nDezena:  {d} \nCentena: {c} \nMilhar:  {m}')