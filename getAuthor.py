import os
import re

def getAuthor(nomFichier):
	titreSeparer = nomFichier.split("_")
	finTitreSeparer = titreSeparer[len(titreSeparer)-1].split(".")
	finTitre = finTitreSeparer[0]

	fichier = open(nomFichier, "r")
	lignes = fichier.readlines()
	fichier.close()


	for i in range(0,len(lignes)):
		if finTitre.lower() in lignes[i].lower():
			y = i+1
			auteurLigne = "Auteur :\n\t"
			while "abstract" not in lignes[y].lower():
				auteurLigne = auteurLigne +" "+ lignes[y].strip()
				y = y + 1
			break

	return auteurLigne
