# -*- coding: latin-1 -*-
#Programa scrabble.py que determina las palabras del diccionario #sowpods.txt que no poseen valores repetidos(consecutivos)
#Autor: Veronica Liñayo 
#Carnet 08-10615
# Versión 1, version iterativa.

import string

ins = open( "sowpods.txt", "r" )
array = []

for line in ins:
    array.append( line )
ins.close()

s = ''.join(array)
a= s.split()
c = ['AA', 'BB','CC', 'DD','EE', 'FF','GG', 'HH','II', 'JJ','KK', 'LL', 'MM', 'NN','OO', 'PP','QQ', 'RR','SS', 'TT','UU', 'VV', 'WW', 'XX','YY', 'ZZ']


i=0
j=0

for i in range(0, len(a)):
    va = 0
    for j in range(0, len(c)):
	if a[i].find(c[j]) != -1:
	   va = 1
    if va:
       continue
    else:
       print 'Is not in:', a[i]
