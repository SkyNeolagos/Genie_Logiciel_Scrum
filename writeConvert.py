import os

def writeConvert(type, nom, titre, auteurs, abstract,introduction,corps,conclusion,discussion, biblio):
    if type.lower() == "xml":
        nomFichier = nom + ".xml"
        debut = "<article>\n"
        nom = "\t<preamble>"+nom+"</preamble>\n"
        titre = "\t<titre>"+titre+"</titre>\n"
        auteurs = "\t<auteur>"+auteurs+"</auteur>\n"
        abstract = "\t<abstract>"+abstract+"</abstract>\n"
        introduction = "\t<introduction>"+introduction+"</introduction>\n"
        corps = "\t<corps>"+corps+"</corps>\n"
        conclusion = "\t<conclusion>"+conclusion+"</conclusion>\n"
        discussion = "\t<discussion>"+discussion+"</discussion>\n"
        biblio = "\t<biblio>"+biblio+"</biblio>\n"
        fin = "</article>\n"

    elif type.lower() == "text":
        nomFichier = nom + ".txt"
        debut = ""
        nom = "Nom du fichier :\n\t"+nom+"\n\n"
        titre = "Titre :\n\t" + titre + "\n\n"
        auteurs = "Auteur :\n\t" + auteurs + "\n\n"
        abstract = "Abstract :\n\t" + abstract + "\n\n"
        introduction = "introduction :\n\t" + introduction + "\n\n"
        corps = "Corps :\n\t" + corps + "\n\n"
        conclusion = "Conclusion :\n\t" + conclusion + "\n\n"
        discussion = "Discussion :\n\t" + discussion + "\n\n"
        biblio = "Bilbiographie :\n\t" + biblio + "\n\n"
        fin = ""

    with open("finalDossier/"+nomFichier, "a") as fichierFinal:
        fichierFinal.write(debut)
        fichierFinal.write(nom)
        fichierFinal.write(titre)
        fichierFinal.write(auteurs)
        fichierFinal.write(abstract)
        fichierFinal.write(introduction)
        fichierFinal.write(corps)
        fichierFinal.write(conclusion)
        fichierFinal.write(discussion)
        fichierFinal.write(biblio)
        fichierFinal.write(fin)
        fichierFinal.close
