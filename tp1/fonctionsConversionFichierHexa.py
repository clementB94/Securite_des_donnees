#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 15:05:20 2020

@author: lacombea
"""

"""
On doit tout d'abord génerer un code de chiffrement, on va aussi utiliser une matrice de codage.
A partir de ces deux éléments, on va additioner modulo 26 les charactères de notre texte avec le code selon la matrice.
si le code de chiffrement est entirèment utilisé on repasse au premier charactère et on continue.
"""
# Librairie nécessaire pour pouvoir utiliser les fonctions ci-dessous
import binascii
import string
import time

##### PARTIE I #####

alphabet = string.ascii_lowercase
dict = {}

for i in range(len(alphabet)):
    row = chr(i+97)
    dict[row] = {}
    for j in range(len(alphabet)):
        col = chr(j+97)
        dict[row][col] = (alphabet[(j+i)%26])


def code(string):
    chiff = ['s', 'k', 'u', 'r', 't']
    code = ''
    for i, char in enumerate(string):
        code += dict[char][chiff[i%len(chiff)]]
    return code

def decode(code):
    chiff = ['s', 'k', 'u', 'r', 't']
    string = ''
    for i, char in enumerate(code):
        for keys, values in dict[chiff[i%len(chiff)]].items():
            if values == char:
                string += keys
    return string

print(code('salutatousjesuisclementboudou'))
print(decode('kkflmsdillbomlbkmfvfwxnshmnil'))


###### PARTIE II ######

hex_alph = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
hex_dict = {}

for indexi, i in enumerate(hex_alph):
    hex_dict[i] = {}
    for indexj, j in enumerate(hex_alph):
        hex_dict[i][j] = hex_alph[(indexj+indexi)%len(hex_alph)]

def fichierVersChaineHexa(fichier):
    """
     
    Parameters
    ----------
    fichier : string
        Un nom de fichier valide et présent sur le disque dur

    Returns
    -------
    chaine_hexa : string
        Une chaîne de caractères contenant la suite des codes hexadécimaux
        correspondant au contenu du fichier "fichier" dont le nom est 
        fourni en paramètre

    """
    handle = open(fichier, 'rb')
    octets = handle.read() 
    hexa = binascii.hexlify(octets)
    handle.close()
    chaine_hexa = hexa.decode('ascii'); 
    return chaine_hexa


###############################################
def chaineHexaVersFichier(chaineHexa, fichier):
    """
 
    Parameters
    ----------
    chaineHexa : string
        Une chaîne de caractères contenant une suite de codes hexadécimaux
        
    fichier : string
        Un nom de fichier à créer sur le disque dur dans lequel sera
        enregistré le contenu binaire correspondant à la suite de codes
        hexadécimaux composant la chaîne "chaineHexa"

    Returns
    -------
    0

    """
    handle = open(fichier, 'wb')
    hexa = chaineHexa.encode()
    octets = binascii.unhexlify(hexa)
    handle.write(octets)
    handle.close()
    return 0


def hexa_code(fichier):
    chiff_hexa = ['0', '1', 'f', 'e', '8']
    chaine_hexa = fichierVersChaineHexa(fichier)
    chaine_hexa_code = ''
    for i, char in enumerate(chaine_hexa):
        chaine_hexa_code += hex_dict[char][chiff_hexa[i%len(chiff_hexa)]]
    return chaine_hexa_code

def hexa_decode(fichier):
    chiff = ['0', '1', 'f', 'e', '8']
    chaine_hexa = fichierVersChaineHexa(fichier)
    chaine_hexa_decode = ''
    for i, char in enumerate(chaine_hexa):
        for keys, values in hex_dict[chiff[i%len(chiff)]].items():
            if values == char:
                chaine_hexa_decode += keys
    return chaine_hexa_decode


start_time = time.time()

chaineHexaVersFichier(hexa_code('Contenus numériques\Bees.mp4'), 'Contenus numériques\Bees_crypto.mp4')
chaineHexaVersFichier(hexa_decode('Contenus numériques\Bees_crypto.mp4'), 'Contenus numériques\Bees_decrypt.mp4')

print("--- %s seconds ---" % (time.time() - start_time))

# Time for Flaubert_decrypt.txt : 2.859 seconds
# Time for Radiographie crane_decrypt.png : 0.744 seconds
# Time for Bees_decrypt.mp4 : 26.53 seconds

# Le ciffrement de Vigenère n'est pas vraiment adapté au fichiers volumineux
