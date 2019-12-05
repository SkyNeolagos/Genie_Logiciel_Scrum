import os

def writeConvert(type, nom, titre, auteurs, abstract, biblio):
    if type.lower() == "xml":
        nomFichier = nom + ".xml"
        debut = "<article>\n"
        nom = "\t<preamble>"+nom+"</preamble>\n"
        titre = "\t<titre>"+titre+"</titre>\n"
        auteurs = "\t<auteur>"+auteurs+"</auteur>\n"
        abstract = "\t<abstract>"+abstract+"</abstract>\n"
        biblio = "\t<biblio>"+biblio+"</biblio>\n"
        fin = "</article>\n"

    elif type.lower() == "text":
        nomFichier = nom + ".txt"
        debut = ""
        nom = "Nom du fichier :\n\t"+nom+"\n\n"
        titre = "Titre :\n\t" + titre + "\n\n"
        auteurs = "Auteur :\n\t" + auteurs + "\n\n"
        abstract = "Abstract :\n\t" + abstract + "\n\n"
        biblio = "Bilbiographie :\n\t" + biblio + "\n\n"
        fin = ""

    with open("finalDossier/"+nomFichier, "a") as fichierFinal:
        fichierFinal.write(debut)
        fichierFinal.write(nom)
        fichierFinal.write(titre)
        fichierFinal.write(auteurs)
        fichierFinal.write(abstract)
        fichierFinal.write(biblio)
        fichierFinal.write(fin)
        fichierFinal.close
