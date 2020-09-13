#O mesmo prof. quer sortear a ordem de apresentação de
# trabalhos. Faça um programa que leia o nome dos 4 alunos
# e mostre a ordem sorteada.

from random import shuffle

a1 = input('Primeiro(a) aluno(a): ')
a2 = input('Segundo(a) aluno(a): ')
a3 = input('Terceiro(a) aluno(a): ')
a4 = input('Quarto(a) aluno(a): ')

ordem = [a1, a2, a3, a4]

shuffle(ordem)

print()
print('-'*30)
print('Apresentação'.center(30))
print('-'*30)
print(f'{ordem}'.center(30))



