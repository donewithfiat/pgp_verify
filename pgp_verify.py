import os

def import_pgp(imp_file):
    system_text = "gpg --import " + imp_file
    os.system(system_text)

def verfiy_pgp(ver_file):
    system_text = "gpg --verify " + ver_file
    os.system(system_text)

imp = input("enter file to import: ")
import_pgp(imp)

ver = input("enter file to verify: ")
verfiy_pgp(ver)
