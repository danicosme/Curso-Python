#Escreva um programa que faça o computador pensar em num inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido. O programa deverá
# escrever na tela de o usuário venceu ou não.

from random import randint

num = randint(1, 10)

usuario = int(input('Escolha um número entre 1 e 10: '))

if num == usuario:
    print('Você venceu! Parabéns.')
else:
    print(f'Eu pensei no número: {num}')
    print('Se lascou, amor! ')
