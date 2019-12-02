def getAbstract(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()

	contenu=""
	if "ABSTRACT" in textComplet :
		tmp,contenu=textComplet.split("ABSTRACT",1)
	elif "Abstract" in textComplet :
		tmp,contenu=textComplet.split("Abstract",1)

	if "INTRODUCTION" in textComplet:
		contenu,tmp=textComplet.split("INTRODUCTION",1)
	elif "Introduction" in textComplet :
		contenu,tmp=textComplet.split("Introduction",1)

	if contenu=="":
		return "Abstract introuvable"

	contenu=contenu.rsplit('1',1)[0]

	while contenu[0].isalpha()==False:
		contenu=contenu[1:]

	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-2]

	contenu=contenu.strip()
	return contenu
