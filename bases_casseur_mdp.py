#!/usr/bin/env python3
# coding:utf8
import sys
import time
import hashlib

mot_de_passe = input("Quel est le mot de passe à deviner : ")  # raw_input évite d'interpréter le contenu fourni
mot_de_passe_md5 = hashlib.md5(mot_de_passe.encode("utf8")).hexdigest()
print(mot_de_passe_md5)


def hash_crack():
    try:
        # mots_fr = open("rockyou.txt", encoding="utf8")
        mots_fr = open("liste_francais.txt")
        trouve = False
        for mot in mots_fr.readlines():
            mot = mot.strip("\n").encode("utf8")
            hashmd5 = hashlib.md5(mot).hexdigest()
            if hashmd5 == mot_de_passe_md5:
                print("Mot de passe trouvé : " + str(mot) + " (" + hashmd5 + ")")
                trouve = True
        if not trouve:
            print("Mot de passe non trouvé :(")
        mots_fr.close()
    except FileNotFoundError:
        print("Erreur ; nom de dossier ou fichier introuvable !")
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)


debut = time.time()
hash_crack()
print("Durée : " + str(time.time() - debut) + " secondes")