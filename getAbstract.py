def isNum(string):
	for char in string:
		if char!="0" and char!="1" and char!="2" and char!="3" and char!="4" and char!="5" and char!="6" and char!="7" and char!="8" and char!="9" :
			return False
	return True

def getAbstract(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()

	contenu=""
	if "ABSTRACT" in textComplet :
		tmp,contenu=textComplet.split("ABSTRACT",1)
	elif "Abstract" in textComplet :
		tmp,contenu=textComplet.split("Abstract",1)

	if "INTRODUCTION" in contenu:
		contenu,tmp=contenu.split("INTRODUCTION",1)
	elif "Introduction" in contenu :
		contenu,tmp=contenu.split("Introduction",1)

	if contenu=="":
		return "Abstract introuvable"

	contenu=contenu.rsplit('1',1)[0]

	while contenu[0].isalpha()==False:
		contenu=contenu[1:]

	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-2]
	
	ff=contenu.find("")
	if ff>0:
		tmp3=contenu[ff:contenu.find('\n',ff)].strip()

		if isNum(tmp3) or (tmp3!="" and textComplet.count(tmp3)>3):
			tmp1,tmp2=contenu.split("",1)
			tmp2=tmp2[tmp2.find('\n'):].strip()
			tmp2=tmp2[tmp2.find('\n'):].strip()
			contenu=tmp1.strip()+"\n"+tmp2
		else:
			tmp1,tmp2=contenu.split("",1)
			contenu=tmp1.strip()+"\n"+tmp2.strip()

	contenu=contenu.strip()
	contenu=contenu.replace("\n"," ")
	return contenu
