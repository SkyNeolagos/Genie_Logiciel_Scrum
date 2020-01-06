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

	if "INTRODUCTION" in textComplet:
		contenu,tmp=textComplet.split("INTRODUCTION",1)
	elif "Introduction" in textComplet :
		contenu,tmp=textComplet.split("Introduction",1)
	elif "I NTRODUCTION" in textComplet:
		contenu,tmp=textComplet.split("I NTRODUCTION",1)


	x=len(contenu)-1
	while contenu[x]!="1" and contenu[x]!="I":
		x=x-1
		if x==0:
			break
	contenu=contenu[:x]
	contenu=contenu.strip()



	if "ABSTRACT" in contenu :
		tmp,contenu=contenu.split("ABSTRACT",1)
	elif "Abstract" in contenu :
		tmp,contenu=contenu.split("Abstract",1)
	elif "A BSTRACT" in contenu :
		tmp,contenu=textComplet.split("A BSTRACT",1)
	else:
		contenu.strip()
		if "\n\n" in contenu:
			tmp,contenu=contenu.rsplit("\n\n",1)

	if contenu[0]==".":
		contenu=contenu[1:]


	if contenu=="":
		return "Abstract introuvable"

	contenu=contenu.strip()


	while "" in contenu:
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
