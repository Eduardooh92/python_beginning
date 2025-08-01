idade = int(input('Digite sua idade: '))

if idade > 0 and idade <= 12:
    print('Você é criança.')
elif idade >= 13 and idade <= 18:
    print('Você é adolescente.')
else:
    print('Você é adulto.')
    