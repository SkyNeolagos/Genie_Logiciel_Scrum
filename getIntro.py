def isNum(string):
	for char in string:
		if char!="0" and char!="1" and char!="2" and char!="3" and char!="4" and char!="5" and char!="6" and char!="7" and char!="8" and char!="9" :
			return False
	return True


def getIntro(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()

	contenu=""
	tmp=""
	if "INTRODUCTION" in textComplet :
		tmp,contenu=textComplet.split("INTRODUCTION",1)
	elif "Introduction" in textComplet :
		tmp,contenu=textComplet.split("Introduction",1)
	
	if tmp=="":
		return "Introduction introuvable"

	tmp=tmp.strip()
	tmp2=tmp[tmp.rfind("\n"):].strip()

	if tmp2=="I.":
		contenu,tmp=contenu.split("\nII.",1)
	elif tmp2=="1.":
		contenu,tmp=contenu.split("\n2.",1)

	elif tmp2=="1":
		contenuBis=contenu
		tmpTest=0
		boucle=True

		while boucle :
			ff=contenuBis.find("2")
			test=contenuBis.find("\n2")
			if ff>0 and ff<test:
				test=ff
			if contenuBis[test+2]==" " or contenuBis[test+2]=="\n" :
				contenu=contenu[:test+tmpTest]
				boucle=False
			else:
				contenuBis=contenuBis[test+2:]
				tmpTest+=test+2			
	else:
		contenu,tmp=contenu.split("\n2\n",1)

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

	if contenu=="":
		return "Introduction introuvable"


	contenu=contenu.strip()

	return contenu