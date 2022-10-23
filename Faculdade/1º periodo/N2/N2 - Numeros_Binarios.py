dividn = int(input('Número na base Decimal: '))
user = dividn
quoci = 1
lista = []

while quoci >= 1:
    rest = dividn % 2
    lista.insert(0, rest)
    quoci = dividn // 2
    dividn = quoci

binary = ''.join([str(item)for item in lista])
print('Conversão na base binário:', binary)
