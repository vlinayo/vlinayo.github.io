# -*- coding: latin-1 -*-
#Programa scrabble.py que determina las palabras del diccionario #sowpods.txt que no poseen valores repetidos(consecutivos)
#Autor: Veronica Liñayo 
#Carnet 08-10615


import string

ins = open( "sowpods.txt", "r" )
array = []
resp= []

for line in ins:
    array.append( line )
ins.close()

s = ''.join(array)

c = ['A', 'B','C', 'D','E', 'F','G', 'H','I', 'J','K', 'L', 'M', 'N','O', 'P','Q', 'R','S', 'T','U', 'V', 'W', 'X','Y', 'Z']

#Mediante filter, hacemos una selección de todos los x que cumplan con la condición dada, tal que para todos los que x, su valor dado sea c, es decir, x serán los distinos valores de c.

resps = filter(lambda x : s.find(x+x) == -1, c)

print list(set(resps))
