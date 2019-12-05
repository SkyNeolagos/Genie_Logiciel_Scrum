import os

def affichage_menu(listFilesPdf):
    os.system('clear')
    longueur = len(listFilesPdf)
    for i in range(0,longueur):
        print i,":",listFilesPdf[i]
 
        
def execute_menu():
    os.system('clear')
    listFiles = os.listdir(".")
    listFilesPdf=[]
    for position in listFiles:
        if position.endswith(".pdf"):
            listFilesPdf.append(position)
    loop = True
    while loop:
        affichage_menu(listFilesPdf)
        choice = input("Entrez le numéro du PDF que vous souhaitez convertir: ")
        print(listFilesPdf[choice])

if __name__ == '__main__':
    execute_menu()
