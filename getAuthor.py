import os
import re

def getAuthor(nomFichier):
	titreSeparer = nomFichier.split("_")
	finTitreSeparer = titreSeparer[len(titreSeparer)-1].split(".")
	finTitre = finTitreSeparer[0]
	
	fichier = open(nomFichier, "r")
	lignes = fichier.readlines()
	fichier.close()
	print nomFichier
	auteurLigne = "Aucun Auteur"
	for i in range(0,len(lignes)):
		if finTitre.lower() in lignes[i].lower():
			y = i+1
			auteurLigne = ""
			while "abstract" not in lignes[y].lower():
				auteurLigne = auteurLigne +" "+ lignes[y].strip()
				if y+1<len(lignes):
					y=y+1
				else:
					break
			break
	return auteurLigne
