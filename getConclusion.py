def getConclusion(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()
	
	contenu=""
	if "CONCLUSION" in textComplet :
		tmp,contenu=textComplet.rsplit("CONCLUSION",1)
	elif "Conclusion" in textComplet :
		tmp,contenu=textComplet.rsplit("Conclusion",1)

	if "REFERENCES" in contenu:
		contenu,tmp=contenu.rsplit("REFERENCES",1)
	elif "References" in contenu :
		contenu,tmp=contenu.rsplit("References",1)

	if "ACKNOWLEDGMENTS" in contenu:
		contenu,tmp=contenu.rsplit("ACKNOWLEDGEMENTS",1)
	elif "Acknowledgements" in contenu :
		contenu,tmp=contenu.rsplit("Acknowledgements",1)

	if contenu=="":
		return "Conclusion introuvable"

	while contenu[0]!="\n":
		contenu=contenu[1:]

	contenu=contenu.strip()
	contenu="Conclusion:\n\t"+contenu

	return contenu+"\n"
