def isNum(string):
	for char in string:
		if char!="0" and char!="1" and char!="2" and char!="3" and char!="4" and char!="5" and char!="6" and char!="7" and char!="8" and char!="9" :
			return False
	return True


def getConclusion(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()
	
	contenu=""
	if "CONCLUSION" in textComplet :
		tmp,contenu=textComplet.rsplit("CONCLUSION",1)
	elif "Conclusion" in textComplet :
		tmp,contenu=textComplet.rsplit("Conclusion",1)
	elif "C ONCLUSION" in textComplet :
		tmp,contenu=textComplet.rsplit("C ONCLUSION",1)

	if "REFERENCES" in contenu:
		contenu,tmp=contenu.rsplit("REFERENCES",1)
	elif "References" in contenu :
		contenu,tmp=contenu.rsplit("References",1)
	elif "R EFERENCES" in contenu:
		contenu,tmp=contenu.rsplit("R EFERENCES",1)

	if "ACKNOWLEDGMENT" in contenu:
		contenu,tmp=contenu.rsplit("ACKNOWLEDGMENT",1)
	elif "Acknowledgement" in contenu :
		contenu,tmp=contenu.rsplit("Acknowledgement",1)
	elif "A CKNOWLEDGMENT" in contenu:
		contenu,tmp=contenu.rsplit("A CKNOWLEDGMENT",1)
	elif "Acknowledgment" in contenu :
		contenu,tmp=contenu.rsplit("Acknowledgment",1)

	if "APPENDIX\n" in contenu:
		contenu,tmp=contenu.rsplit("APPENDIX\n",1)
	elif "Appendix\n" in contenu :
		contenu,tmp=contenu.rsplit("Appendix\n",1)


	if contenu=="":
		return "Conclusion introuvable"

	while contenu[0]!="\n":
		contenu=contenu[1:]

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
	return contenu
