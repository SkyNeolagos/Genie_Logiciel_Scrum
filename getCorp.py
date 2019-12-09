def getCorp(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()

	contenueIntro = getIntro(mon_fichier)
	contenueIntro = contenueIntro[len(contenueIntro)-10:]

	if contenueIntro in contenu :
		tmp,contenu=contenu.split(contenueIntro,1)


	if "DISCUSSION" in contenu :
		contenu,tmp=contenu.split("DISCUSSION",1)
	elif "Discussion" in contenu :
		contenu,tmp=contenu.split("Discussion",1)
	elif "Conclusions" in contenu:
		contenu,tmp=contenu.split("Conclusions",1)
	elif "Conclusion" in contenu :
		contenu,tmp=contenu.split("Conclusion",1)


	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-1]

	contenu=contenu.strip()
	return contenu