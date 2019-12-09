from converter import *
from getAbstract import *
from getTitre import *
from getAuthor import *
from getBiblio import *
from getConclusion import *
from getIntroduction import *
from getDiscussion import *
from writeConvert import *
from getArgument import *
import os

def createFolderFinal():
    repertoire = 'finalDossier'
    if(os.path.exists(repertoire)==False):
        os.mkdir(repertoire)
    else:
        consoleCommand='rm -r '+repertoire
        os.system(consoleCommand)
        os.mkdir(repertoire)

def rmFolderConvert():
	repertoire = 'convertDossier'
	if(os.path.exists(repertoire)==True):
		consoleCommand='rm -r '+repertoire
		os.system(consoleCommand)

def setup():
    if convertToTxt() == "resume":
	    listFilesTxt=os.listdir("convertDossier")
	    ##pathDirectory=os.path.dirname(os.path.abspath(__file__))+"/convertDossier"
	    createFolderFinal()
	    for pos in listFilesTxt:
		if pos.endswith(".txt"):
		chemin="convertDossier/"+pos
		titre=getTitre(chemin)
                auteur=getAuthor(chemin)
		abstract=getAbstract(chemin)
		introduction=getIntro(chemin)
                corps=#getCorps(chemin)
                conclusion=getConclusion(chemin)
                discussion=getDiscussion(chemin)
		biblio=getBiblio(chemin)
		nom=os.path.splitext(os.path.basename(pos))[0]
		writeConvert(getArgument(),nom,titre,auteur,abstract,introduction,corps,conclusion,discussion,biblio)
	    rmFolderConvert()
