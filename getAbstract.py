

def Abstract(mon_fichier):
	mon_fichier = open(mon_fichier, "r")
	contenu = mon_fichier.read()
	mon_fichier.close()

	try:
		tmp,contenu=contenu.split("ABSTRACT",1)
	except ValueError:
		tmp,contenu=contenu.split("Abstract",1)

	try:
		contenu,tmp=contenu.split("INTRODUCTION",1)
	except ValueError:
		contenu,tmp=contenu.split("Introduction",1)

	contenu=contenu.rsplit('1',1)[0]

	if contenu[0].isalpha()==False:
		contenu=contenu[1:]

	contenu=contenu.strip()
	contenu="Abstract:\n\t"+contenu
	print(contenu)

if __name__ == '__main__':
	Abstract("text1.txt")
