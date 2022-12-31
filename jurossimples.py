t = input('Tempo:')
i = input('Taxa:')
c = input('Capital:')
porcentagem = float(i) / 100
j = float(c) * float(porcentagem) * float(t)

## Montante

m = float(c) + float(j)


print('Juros:',j)

print('Montante', m)