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

