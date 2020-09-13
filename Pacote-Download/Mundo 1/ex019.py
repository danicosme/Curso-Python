#Um prof quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = input('Primeiro(a) aluno(a): ')
a2 = input('Segundo(a) aluno(a): ')
a3 = input('Terceiro(a) aluno(a): ')
a4 = input('Quarto(a) aluno(a): ')


escolha = [a1, a1, a3, a4]


print(f'\nPessoa escolhida: {choice(escolha)}')