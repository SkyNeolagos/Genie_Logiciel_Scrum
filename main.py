from converter import *
from getAbstract import *
from getTitre import *
from getAuthor import *
from getBiblio import *
from writeConvert import *

import os

def createFolderFinal():
    repertoire = 'finalDossier'
    if(os.path.exists(repertoire)==False):
        os.mkdir(repertoire)
    else:
        consoleCommand='rm -r '+repertoire
        os.system(consoleCommand)
        os.mkdir(repertoire)

def main():
    convertToTxt()
    listFilesTxt=os.listdir("convertDossier")
    ##pathDirectory=os.path.dirname(os.path.abspath(__file__))+"/convertDossier"
    createFolderFinal()
    for pos in listFilesTxt:
        if pos.endswith(".txt"):
            chemin="convertDossier/"+pos
            titre=getTitre(chemin)
            abstract=getAbstract(chemin)
            auteur=getAuthor(chemin)
            biblio=getBiblio(chemin)
            nom=os.path.splitext(os.path.basename(pos))[0]

            writeConvert("text",nom,titre,auteur,abstract,biblio)



if __name__ == '__main__':
    main()
