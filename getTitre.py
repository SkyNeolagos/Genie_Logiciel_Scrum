import os
import re

def getTitre(nomFichier):
	with open(nomFichier, "r") as fichierOrigin:
		titre = fichierOrigin.readline()
		fichierOrigin.close
	with open("final"+nomFichier, "a") as fichierDestination:
		fichierDestination.write("Titre:\n")
		fichierDestination.write("\t"+titre)
		fichierDestination.close

if __name__ == '__main__':
	getTitre("data.txt")