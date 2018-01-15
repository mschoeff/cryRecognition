import os
import numpy as np

#Funktion um einzelnen Ordner zu erstellen
def createSingleFolder(path, name):
    if not os.path.exists(path + "/" + name):
        os.makedirs(path + "/" + name)
    return None

#Funktion um Zielordner fuer Speicherung zu erstellen
def createOutPutFolders(outputPath, parameter):
    createSingleFolder(outputPath, parameter.operations + "-Daten")
    return None

#Funktion zur Abspeicherung der extrahierten Features
def saveFeatures(value, parameter, outputFolder, filename):

    datafile = open(outputFolder + '/' + parameter.operations + "-Daten"+ '/' + filename + '_' + parameter.operations + '_data', 'wb')
    np.save(datafile, value)
    return None