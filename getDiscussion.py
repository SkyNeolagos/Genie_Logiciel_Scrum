def getDiscussion(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()


	if "DISCUSSION" in contenu :
		tmp,contenu=contenu.split("DISCUSSION",1)
	elif "Discussion" in contenu :
		tmp,contenu=contenu.split("Discussion",1)
	elif "D ISCUSSION" in contenu :
		tmp,contenu=contenu.split("D ISCUSSION",1)
	else:
		return "Aucune Discussion presente dans le Pdf d'origine."


	if "CONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("CONCLUSIONS",1)
	elif "Conclusion" in contenu :
		contenu,tmp=contenu.rsplit("Conclusion",1)
	elif "C ONCLUSIONS" in contenu:
		contenu,tmp=contenu.rsplit("C ONCLUSIONS",1)

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


	while contenu[0]!="\n":
		contenu=contenu[1:]


	while contenu[len(contenu)-1]!="\n":
		contenu=contenu[:len(contenu)-1]

	contenu=contenu.strip()
	return contenu
