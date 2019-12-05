def getDiscussion(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()


	if "DISCUSSION" in contenu :
		tmp,contenu=contenu.split("DISCUSSION",1)
	elif "Discussion" in contenu :
		tmp,contenu=contenu.split("Discussion",1)

	if "Conclusions" in contenu:
		contenu,tmp=contenu.split("Conclusions",1)
	elif "Conclusion" in contenu :
		contenu,tmp=contenu.split("Conclusion",1)

	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-1]

	contenu=contenu.strip()
	return contenu
