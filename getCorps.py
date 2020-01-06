from getIntro import *

def getCorp(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()


	textComplet=contenu
	contenu=""
	tmp=""
	if "INTRODUCTION" in textComplet :
		tmp,contenu=textComplet.split("INTRODUCTION",1)
	elif "Introduction" in textComplet :
		tmp,contenu=textComplet.split("Introduction",1)
	elif "I NTRODUCTION" in textComplet :
		tmp,contenu=textComplet.split("I NTRODUCTION",1)
	
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
	elif "\n2\n" in textComplet:
		contenu,tmp=contenu.split("\n2\n",1)
	else:
		return "Introduction introuvable"

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

	if contenu=="":
		return "Introduction introuvable"


	contenueIntro=contenu.strip()

	contenu=textComplet

	if len(contenueIntro)>30:
		contenueIntro = contenueIntro[len(contenueIntro)-20:]

	if contenueIntro in contenu :
		tmp,contenu=contenu.split(contenueIntro,1)


	if "DISCUSSION" in contenu :
		contenu,tmp=contenu.rsplit("DISCUSSION",1)
	elif "Discussion" in contenu :
		contenu,tmp=contenu.rsplit("Discussion",1)
	elif "D ISCUSSION" in contenu :
		contenu,tmp=contenu.rsplit("D ISCUSSION",1)
	if "CONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("CONCLUSIONS",1)
	elif "Conclusion" in contenu :
		contenu,tmp=contenu.rsplit("Conclusion",1)
	elif "C ONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("C ONCLUSIONS",1)

	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-1]

	contenu=contenu.strip()
	
	return contenu
