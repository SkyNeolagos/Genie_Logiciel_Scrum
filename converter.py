import os ##Librairie operating systems
import re

def convertToTxt():
    listFilesPdf=os.listdir('.')
    pathDirectory=os.path.dirname(os.path.abspath(__file__))
    for pos in listFilesPdf:
        if pos.endswith(".txt"):
            os.remove(os.path.join(pathDirectory,pos))
        if pos.endswith(".pdf"):
            name=os.path.splitext(os.path.basename(pos))[0]
            replace=pos.replace(' ','_')
            os.rename(pos,replace)
            consoleCommand='pdftotext '+replace+' '+name+'.txt'
            os.system(consoleCommand)
if __name__ == '__main__':
    convertToTxt()
