import math


b = input('Valor do cateto 1:' )
c = input('Valor do cateto 2:')

r = float(b)**2 + float(c)**2

a = math.sqrt(r)

print('b^2 + c^2 = ', r, 'diferente de a')
print('Hipotenusa:', a)