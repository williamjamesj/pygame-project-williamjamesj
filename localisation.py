import globalvariables as globals
def readlang():
    try:
        f = open("resources/localisation/lastlang", "r")
        globals.lang = f.readline()
    except Exception as E:
        globals.lang = "english"
    return
def setlang(language):
    f = open("resources/localisation/lastlang","w")
    f.write(language)
    return
def readtexts():
    try:
        f = open(f"resources/localisation/{globals.lang}","r")
        languagesdict = {}
        for i in f:
            key, value = i.split(":")
            languagesdict[key] = value.rstrip()
        globals.languagesdict = languagesdict
    except Exception as E:
        globals.languagesdict = {}
    return
