def getDiscussion(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()


	if "DISCUSSION" in contenu :
		tmp,contenu=contenu.split("DISCUSSION",1)
	elif "Discussion" in contenu :
		tmp,contenu=contenu.split("Discussion",1)
	elif "D ISCUSSION" in contenu :
		tmp,contenu=contenu.split("D ISCUSSION",1)
	else:
		return "Aucune Discussion presente dans le Pdf d'origine."


	if "CONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("CONCLUSIONS",1)
	elif "Conclusion" in contenu :
		contenu,tmp=contenu.rsplit("Conclusion",1)
	elif "C ONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("C ONCLUSIONS",1)

	while contenu[0]!="\n":
		contenu=contenu[1:]


	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-1]

	contenu=contenu.strip()
	return contenu
