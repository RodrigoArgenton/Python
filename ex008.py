#variavel de medida com a finalidade de conversão.
metros = float(input('Digite uma distância em metros:  '))

#variaveis de conversão
k = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

#imprimindo resultado dos valores de medida.
print(f'A medida de {metros}m correspode a: ')
print(f'{k}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')