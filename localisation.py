import globalvariables as globals
def readlang():
    f = open("resources/localisation/lastlang", "r")
    globals.lang = f.readline()
def setlang(language):
    f = open("resources/localisation/lastlang","w")
    f.write(language)
def readtexts():
    f = open(f"resources/localisation/{globals.lang}","r")
    languagesdict = {}
    for i in f:
        key, value = i.split(":")
        languagesdict[key] = value.rstrip()
    globals.languagesdict = languagesdict