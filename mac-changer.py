import subprocess
import random 
import string
import regex as re

def show_current_network_config():
    cmdCommand = "ipconfig"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if output:
        try:
            print(output.decode('cp1252'))
        except UnicodeDecodeError:
            print(output.decode('cp1252', errors='ignore'))
    if error:
        print("Erreur:", error.decode('cp1252', errors='ignore'))

print("Pour voir votre configuration réseau, veuillez taper 1")

nombre_choisi = input()

if nombre_choisi == '1':
    show_current_network_config()