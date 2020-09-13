#Faça um ex que leia algo e informe tudo sobre:
'''
Maiúsculo
Minúsculo
Alfanum
Alfabético
ASCII
DECIMAL
DIGITO
IDENT
PRINT
SÓ TEM ESPAÇO?
ESTÁ CAPITALIZADO?
'''

algo = input('Digite algo: ')

print('É maiúsculo:',algo.isupper())
print('É minúsculo: ',algo.islower())
print('É alfanumérico: ',algo.isalnum())
print('É alfabético: ',algo.isalpha())
print('É ASCII: ',algo.isascii())
print('É decimal: ',algo.isdecimal())
print('É dígito: ',algo.isdigit())
print('É identificador: ',algo.isidentifier())
print('É printável: ',algo.isprintable())
print('Só tem espaço: ',algo.isspace())
print('É título: ',algo.istitle())


