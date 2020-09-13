#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantos A,
# primeira posição do A
# última posição do A.

frase = input('Frase: ').strip().upper()

print(f'Quantas letras A: {frase.count("A")}')
print(f'Posição do primeiro A: {frase.find("A")+1}')
print(f'Posição do último A: {frase.rfind("A")}')