import numpy as np
from CreateFolders import *
from InOut import *
from ParameterCheck import *
from getOperations import *
from computeSpectralFeatures import *
from Normalisierungsfunktionen import *
import parameter

#Funktion zur Durchfuehrung der spezifischen Extraktion und Speicherung der Daten
def extractionOfFeatures(parameter, y):

    feature = parameter.operationDictionary[parameter.operations](y, parameter)

    return feature


#Funktion zur Abspeicherung der extrahierten Features
def saveFeatures(value, parameter, outputFolder, filename):

    datafile = open(outputFolder + '/' + parameter.operations + "-Daten"+ '/' + filename + '_' + parameter.operations + '_data', 'wb')
    np.save(datafile, value)


    return None


#Extraktionsfunktion
def extract(inputFolder, outputFolder, parameter, stringList):

    print(parameter.operations)
    parameter.setOperations(stringList)
    print(parameter.operations)
    print(capitalizeStrings(stringList))
    #parameter.checkIntegrity()

    audioList = listAudios(inputFolder)
    createOutPutFolders(outputFolder, parameter)

    #MFCCMatrix = createMFCCMatrix(audioList, parameter)
    normalizationArray = np.empty([parameter.normalizationDictionary[parameter.operations], 1])
    timeframeSum = 0
    print(np.shape(normalizationArray))

    #to do mittwoch: np.absolute() verwenden um in array zu schreiben

    for file in audioList:
        y, sr, filename = readInAudio(inputFolder, file)
        feature = extractionOfFeatures(parameter, y)
        print(feature.shape)
        saveFeatures(feature, parameter, outputFolder, filename)
    #calcNormalizationFactor(MFCCMatrix, outputFolder)

    return None
