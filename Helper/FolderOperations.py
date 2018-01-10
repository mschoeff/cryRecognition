import os

#Funktion um einzelnen Ordner zu erstellen
def createSingleFolder(path, name):
    if not os.path.exists(path + "/" + name):
        os.makedirs(path + "/" + name)
    return None

#Funktion um Zielordner fuer Speicherung zu erstellen
def createOutPutFolders(outputPath, parameter):
    createSingleFolder(outputPath, parameter.operations + "-Daten")
    return None
