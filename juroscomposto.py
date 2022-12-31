c = input('Capital:')
i = input('Taxa de Juros:')
t = input('Tempo:')

porcentagem = float(i) / 100
seg = 1 + float(porcentagem)
hj = float(seg) ** float(t)

m = float(c) * float(hj)

j = float(m) - float(c)

print('Montante:', m)
print('Juros:', j)
