import math

a = input('Valor de a ?')
b = input('valor de b ?')
c = input('valor de c ?')

delta =  float( b )**2  + float(-4) * float( a ) * float( c )

## primeira raiz
raiz = math.sqrt(delta)

pum = - float( b ) + float( raiz )
pdois = 2 * float( a )

xuno = float( pum ) / float(pdois)

## segunda raiz
puno = -float(b) - float(raiz)
pdos =  float(2) * float(a)

xdos = float(puno) / float(pdos)

## Resultado
print('Primeira Raiz : ', xuno)
print ('Segunda Raiz :', xdos)
print('Delata :',delta)