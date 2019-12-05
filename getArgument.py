import sys

def getArgument():
    type = "text"
    for arg in sys.argv:
        if arg == "-t":
            break
        elif arg == "-x":
            type = "xml"
            break

    return type
