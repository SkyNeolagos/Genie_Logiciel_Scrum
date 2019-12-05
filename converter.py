import os ##Librairie operating systems
import re

def createFolder():
    repertoire = 'convertDossier'
    if(os.path.exists(repertoire)==False):
        os.mkdir(repertoire)
    else:
        consoleCommand='rm -r '+repertoire
        os.system(consoleCommand)
        os.mkdir(repertoire)

def convertToTxt():
	if os.path.exists("Papers") == True:
		listFilesPdf=os.listdir("Papers")
		pathDirectory=os.path.dirname(os.path.abspath(__file__))
		createFolder()
		for pos in listFilesPdf:
			if pos.endswith(".txt"):
				os.remove(os.path.join(pathDirectory,pos))
			if pos.endswith(".pdf"):
				name=os.path.splitext(os.path.basename(pos))[0]
				pos="Papers/"+pos
				replace=pos.replace(' ','_')
				os.rename(pos,replace)
				consoleCommand='pdftotext '+replace+' '+'convertDossier/'+name+'.txt'
				os.system(consoleCommand)
		return "resume"
	else:
		return "stop"

def convertTotxtWithName(fichier):
    pathDirectory=os.path.dirname(os.path.abspath(__file__))
    if fichier.endswith(".txt"):
        os.remove(os.path.join(pathDirectory,fichier))
    if fichier.endswith(".pdf"):
        name=os.path.splitext(os.path.basename(fichier))[0]
        replace=fichier.replace(' ','_')
        os.rename(fichier,replace)
        consoleCommand='pdftotext '+replace+' '+name+'.txt'
        os.system(consoleCommand)
