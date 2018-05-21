# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:17:19 2018

@author: edna
"""
#recorrer las claves
#dict1={1:'hola',2:'monn'}
#for clave in dict1.keys():
#    print(clave)

#recorrer valores
#for valor in dict1.values():
#    print(valor)
    
#recorrer ambas
#for clave,valor in dict1.items():
#    print(clave,"->",valor)
 
#repeticion de palabras 
#dict = {}
#frase = input("Frase:")
#lista_palabras=frase.split(" ")
#for palabra in lista_palabras:
#	if palabra in dict:
#		dict[palabra]+=1
#	else:
#		dict[palabra]=1	
#
#for campo,valor in dict.items():
#	print (campo,"->",valor)
    
#codigo morse
#codigo = {
#    'A': '.-',     'B': '-...',    'C': '-.-.',
#    'D': '-..',    'E': '.',       'F': '..-.',
#    'G': '--.',    'H': '....',    'I': '..',
#    'J': '.---',   'K': '-.-',     'L': '.-..',
#    'M': '--',     'N': '-.',      'O': '---',
#    'P': '.--.',   'Q': '--.-',    'R': '.-.',
#    'S': '...',    'T': '-',       'U': '..-',
#    'V': '...-',   'W': '.--',     'X': '-..-',
#    'Y': '-.--',   'Z': '--..',    '1': '.----',
#    '2': '..---',  '3': '...--',   '4': '....-',
#    '5': '.....',  '6': '-....',   '7': '--...',
#    '8': '---..',  '9': '----.',   '0': '-----',
#    '.': '.-.-.-', ',': '--..--',  ':': '---...',
#    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
#    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
#    '-': '-....-', '/': '-..-.',   '=': '-...-',
#    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
#    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
#}	
#
#palabra = input("Palabra:")
#lista_codigos = []
#for caracter in palabra:
#	if caracter.islower():
#		caracter=caracter.upper()
#	lista_codigos.append(codigo[caracter])	
#print (" ".join(lista_codigos))

#gustos
gustos={}
nombre = input("Nombre:")
while nombre!="*":
	gusto=input("Gusto:")
	lista_gustos=gustos.setdefault(nombre,[gusto])
	if lista_gustos!=[gusto]:
		gustos[nombre].append(gusto)
	nombre = input("Nombre:")
print(gustos)