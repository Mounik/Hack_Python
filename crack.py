#!/usr/bin/env python3
# coding:utf8
import sys
import time
import hashlib
import argparse

parser = argparse.ArgumentParser(description="Password Cracker")
parser.add_argument("-f", "--file", dest="file", help="Path of the dictionary file", required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Generate MD5 hash of password", required=False)
parser.add_argument("-md5", dest="md5", help="Hashed password (MD5)", required=False)

args = parser.parse_args()


def crack_dict(md5, file):
    try:
        trouve = False
        for mot in file.readlines():
            mot = mot.strip("\n").encode("utf8")
            hashmd5 = hashlib.md5(mot).hexdigest()
            if hashmd5 == md5:
                print("Mot de passe trouvé : " + str(mot) + " (" + hashmd5 + ")")
                trouve = True
        if not trouve:
            print("Mot de passe non trouvé :(")
        file.close()
    except FileNotFoundError:
        print("Erreur ; nom de dossier ou fichier introuvable !")
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)


debut = time.time()

if args.md5:
    print("[CRACKING HASH " + args.md5 + "]")
    if args.file:
        print("[USING DICTIONARY FILE " + args.file + "]")
        crack_dict(args.md5, open(args.file))

print("Durée : " + str(time.time() - debut) + " secondes")