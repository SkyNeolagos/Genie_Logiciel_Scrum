import os
import re

def getTitre(nomFichier):
	titreSeparer = nomFichier.split("_")
	debTitre = titreSeparer[2]
	finTitreSeparer = titreSeparer[len(titreSeparer)-1].split(".")
	finTitre = finTitreSeparer[0]


	fichier = open(nomFichier, "r")
	lignes = fichier.readlines()
	fichier.close()
	titreFinal=""
	for i in range(0,len(lignes)):
		if debTitre in lignes[i] and finTitre in lignes[i]:
			titreFinal = lignes[i]
			break
		elif debTitre.lower() in lignes[i].lower():
			titreFinal = lignes[i].rstrip()
			y = i+1
			while finTitre.lower() not in lignes[y].lower():
				titreFinal = titreFinal +" "+ lignes[y].rstrip()
				y = y + 1
			titreFinal = titreFinal +" "+ lignes[y].rstrip()
			break
	return titreFinal
