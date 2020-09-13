#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e último nome separadamente.
# Ex: Ana Maira de Souza 
#  Ana Souza

nome = input('Nome completo: ').split()

print(f'{nome[0]} {nome[len(nome)-1]}')

