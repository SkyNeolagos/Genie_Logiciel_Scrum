from converter import *
from getAbstract import *
from getTitre import *
from getAuthor import *
from getBiblio import *
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
            with open("finalDossier/"+nom, "a") as fichierFinal:
                nom="\t<preamble>"+nom+"</preamble>\n"
                titre="\t<titre>"+titre+"</titre>\n"
                auteur="\t<auteur>"+auteur+"</auteur>\n"
                abstract="\t<abstract>"+abstract+"</abstract>\n"
                biblio="\t<biblio>"+biblio+"</biblio>\n"
                fichierFinal.write("<article>\n")
                fichierFinal.write(nom)
                fichierFinal.write(titre)
                fichierFinal.write(auteur)
                fichierFinal.write(abstract)
                fichierFinal.write(biblio)
                fichierFinal.write("</article>\n")
                fichierFinal.close



if __name__ == '__main__':
    main()
