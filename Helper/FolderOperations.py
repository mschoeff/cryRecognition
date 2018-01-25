import os
import numpy as np

def createSingleFolder(path, name):
    if not os.path.exists(path + "/" + name):
        os.makedirs(path + "/" + name)
    return None

def createOutPutFolders(outputPath, parameter):
    createSingleFolder(outputPath, parameter.operations + "-Daten")
    return None

def saveFeatures(value, parameter, outputFolder, filename):

    datafile = open(outputFolder + '/' + parameter.operations + "-Daten"+ '/' + filename + '_' + parameter.operations + '_data', 'wb')
    np.save(datafile, value)
    return None