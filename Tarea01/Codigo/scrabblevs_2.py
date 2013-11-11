# -*- coding: latin-1 -*-
#Programa scrabble.py que determina las palabras del diccionario #sowpods.txt que no poseen valores repetidos(consecutivos)
#Autor: Veronica Liñayo 
#Carnet 08-10615
# Versión 2 usando expresiones regulares.

import sys
import re
import string

ins = open( "sowpods.txt", "r" )
array = []

for line in ins:
    array.append( line )
ins.close()

s = ''.join(array)
a= s.split()

# Se propone la expresión regular: Cualquier cosa + una tupla de #iguales + cualquier cosa. La complilo y guardo en la variable p.
c = '.*(AA|BB|CC|DD|EE|FF|GG|HH|II|JJ|KK|LL|MM|NN|OO|PP|QQ|RR|SS|TT|UU|VV|WW|XX|YY|ZZ).*'

#Luego le pregunto a p si logra reconocer caada uno de los strings del #arreglo
p = re.compile(c)
new_s = filter(lambda x: not p.match(x), a)
print new_s


