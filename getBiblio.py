def isNum(string):
	for char in string:
		if char!="0" and char!="1" and char!="2" and char!="3" and char!="4" and char!="5" and char!="6" and char!="7" and char!="8" and char!="9" :
			return False
	return True

def getBiblio(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()
	contenu=""
	if "REFERENCES" in textComplet :
		tmp,contenu = textComplet.rsplit("REFERENCES\n",1)
	elif "References" in textComplet :
		tmp,contenu = textComplet.rsplit("References\n",1)

	if contenu=="":
		return "References introuvables"
	
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
	return contenu
