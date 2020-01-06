# -*- coding: utf-8 -*-
import os
from setup import *
def affichageListPdf(listFilesPdf):
    os.system('clear')
    longueur = len(listFilesPdf)
    for i in range(0,longueur):
        print (i,":",listFilesPdf[i])

def menuListPdf():
    os.system('clear')
    listFiles = os.listdir("Papers")
    listFilesPdf=[]
    for position in listFiles:
        if position.endswith(".pdf"):
            listFilesPdf.append(position)
    loop = True
    while loop:
        affichageListPdf(listFilesPdf)
        choice = input("Entrez le numéro du PDF que vous souhaitez convertir: ")
        print(listFilesPdf[choice])
        loop=False


def menuPrincipal():
    os.system('clear')
    while True:
        print("Bonjour\n")
        choice=input("Que voulez-vous faire ?\n Entrez le numero correspondant a votre choix:\n\t1:Convertir tous les pdf present dans Papers\n\t2:Convertir certains des pdf present dans Papers\n\t3:Quitter\n")
        if(choice==1):
            setup()
            break
        elif(choice==2):
            menuListPdf()
            break
        else:
            break

def main():
    menuPrincipal()


if __name__ == '__main__':
    main()
