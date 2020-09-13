#Crie um programa que leia o nome completo e mostre:
# O nome com todas as letras maiúsculas,
# o nome com todas minúsculas,
# quantas letras sem considerar espaços,
# quantas letras tem o primeiro nome

nome = input('Nome completo: ')

print()
print('-'*30)
print('Manipulação de string'.center(30))
print('-'*30)
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Quantidade de letras: {len(nome.strip())}')
print(f'Quantidade de letras no primeiro nome: {nome.split()[0]}')