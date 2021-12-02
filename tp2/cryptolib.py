#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed May 13 19:41:22 2020

@author: lacombea

    Module de chiffrement chiffrement.
    
    
"""
import sys
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
class hachage():
    """
    
    Classe de hachage supportant les fonctions de hachage suivantes :\n 
        - md5,
        - sha1,
        - sh224,
        - sha256,
        - sha384,
        - sha512
    
    """

    @staticmethod
    def hashcoder(contenu, nomHash):

        """
        
        Parameters
        ----------
        contenu : TYPE string (encodage utf-8)
            DESCRIPTION.
        Contenu dont on souhaite obtenir le hashcode
        
        nomHash : TYPE string
            DESCRIPTION.
        Nom de la fonction de hachage à utiliser parmi :
            - md5
            - sha1
            - sh224
            - sha256
            - sha384
            - sha512

        Returns
        -------
        hashcodeHEXA TYPE string
            DESCRIPTION.
        Hashcode du contenu sous la forme d'une
        suite de caractères hexadécimaux

        """
        if not(nomHash == 'md5' or nomHash == 'md5' or nomHash == 'sha1' or nomHash == 'sha224' or nomHash == 'sha256' or nomHash == 'sha384'or nomHash == 'sha512'):
            print('La valeur de l\'opérateur de hashage fourni en paramètre de la méthode hachcoder() n\'est pas reconnu. Seules les valeurs "md5" "sha1" "sha224" "sha256" "sha384" et "sha512" sont autorisées.')
            sys.exit()
        if (nomHash == 'md5'):
            hachage.hashcodeHEXA = md5(bytes(contenu, 'utf-8')).hexdigest()
        elif (nomHash == 'sha1'):
            hachage.hashcodeHEXA = sha1(bytes(contenu, 'utf-8')).hexdigest()
        elif (nomHash == 'sha224'):
            hachage.hashcodeHEXA = sha224(bytes(contenu, 'utf-8')).hexdigest()
        elif (nomHash == 'sha256'):
            hachage.hashcodeHEXA = sha256(bytes(contenu, 'utf-8')).hexdigest()
        elif (nomHash == 'sha384'):
            hachage.hashcodeHEXA = sha384(bytes(contenu, 'utf-8')).hexdigest()
        elif (nomHash == 'sha512'):
            hachage.hashcodeHEXA = sha512(bytes(contenu, 'utf-8')).hexdigest()
        return hachage.hashcodeHEXA