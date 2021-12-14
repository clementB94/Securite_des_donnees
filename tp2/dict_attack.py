import csv
from os import read
from cryptolib import hachage

f = open('dico_francais_etendu\dico_francais_etendu.txt', 'r')
read_data = f.read()
f.close()
word_dict = read_data.split('\n')

f = open('utilisateurs_ANSI.csv')
user_dict = csv.DictReader(f)

liste_hashcodes = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

last_word_dict = word_dict[-1]
last_hash_type = liste_hashcodes[-1]

for row in user_dict:

    login = row['login']
    mdp_hash = row['mdp_hash']
    nom = row['nom']
    prenom = row['prenom']
    found_pwd = False
    pwd = ""
    dictw = 'xxx'
    dict_index = 0

    while ((found_pwd == False) and (dictw != last_word_dict)):

        dictw = word_dict[dict_index]
        hash_list_index = 0
        hash_use = 'xxx'

        while hash_use != last_hash_type:

            hash_use = liste_hashcodes[hash_list_index]
            dictw_hash = hachage.hashcoder(dictw, hash_use)

            if dictw_hash == mdp_hash:

                found_pwd = True
                pwd = dictw
                print(login, prenom, nom, mdp_hash, pwd, hash_use)
            
            hash_list_index += 1

        dict_index += 1

    
# bacheletg George Bachelet 8290c438b053682b46756193dc613ea1db7069bf973f65e0848a4bf23e2f3296 intergouvernementale04 sha256
# briominf Franï¿½oise Briomin 46b2f3aab78b094b9dbf791d92c2fc8a68bcae494b1be5f326fc7904e84ef910 anticonstitutionnel01 sha256
# dumontr Renï¿½ Dumont eaf5835612bb00cd3f57ea281bbe3899fb9a267b6421295929a21ffbf8272069 artificiellement00 sha256
# dupontj Josette Dupont 5ddcb42a5b0652c3e10e34d0a29c9057bc94a94ff1ff797266760569bf51f2fb approximativement05 sha256
# lajauniep Patrick Lajaunie 5aebbb4be45d8f94ed7704b1c57c8e4ef7c1aba21912e0c0aa3883bdb4e89b77 architectonique05 sha256
# lambertf Fabienne Lambert 3e69fe5f88e830f52c2e5fac0c9ebde4ce48c97da28810fec92d535fa2eb3f1e aristocratiquement05 sha256
# legrandj Jï¿½rï¿½mie Legrand 4e6feb253456f63409995c8a7b7d2dbe62019262eac5def2ec3b562a47039cb3 Sihanouk03 sha256
# lemaireb Bï¿½atrice Lemaire a0dd6e18fcfc05dfb599976e8f6a62e0fd78695f41253a2425d0f61c9070f21a show-business03 sha256
# martinoa Alain Martino 9e9ac1ec6ce6a3a1c2ecb879fbf4fa1562f4374108518f3593db3413aba57e1b Schnitzler02 sha256
# micheletr Raoul Michelet 895f6ca4ad04ca694fbcd17fc50de2d3bad1d8972ac15cdfc6040f9674c0cfa0 moissonneuse-batteuse sha256
#valettes Sophie Valette 1376a06be4eea216ad119ae19352984bb7992ce7a4a0fdbcb36758d2090455ab Berlusconi00 sha256 

