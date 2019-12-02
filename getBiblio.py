def getBiblio(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	textComplet = mon_fichier.read()
	mon_fichier.close()

	try:
		tmp,contenu=textComplet.rsplit("REFERENCES\n",1)
	except ValueError:
		tmp,contenu=textComplet.rsplit("References\n",1)

	ff=contenu.find('')

	if ff>0:
		tmp3=contenu[ff:contenu.find('\n',ff)].strip()

		if unicode(tmp3).isnumeric() or (tmp3!="" and textComplet.count(tmp3)>1):
			tmp1,tmp2=contenu.split("",1)
			tmp2=tmp2[tmp2.find('\n'):].strip()
			tmp2=tmp2[tmp2.find('\n'):].strip()
			contenu=tmp1.strip()+"\n"+tmp2
	contenu=contenu.strip()
	contenu="References:\n\t"+contenu
	return contenu
