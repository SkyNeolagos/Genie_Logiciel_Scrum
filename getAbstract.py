def getAbstract(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()


	if "ABSTRACT" in contenu :
		tmp,contenu=contenu.split("ABSTRACT",1)
	elif "Abstract" in contenu :
		tmp,contenu=contenu.split("Abstract",1)

	if "INTRODUCTION" in contenu:
		contenu,tmp=contenu.split("INTRODUCTION",1)
	elif "Introduction" in contenu :
		contenu,tmp=contenu.split("Introduction",1)

	contenu=contenu.rsplit('1',1)[0]

	while contenu[0].isalpha()==False:
		contenu=contenu[1:]

	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-2]

	contenu=contenu.strip()
	contenu="Abstract:\n\t"+contenu
	return contenu
