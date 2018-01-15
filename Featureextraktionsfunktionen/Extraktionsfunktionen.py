import numpy as np
import FolderOperations
import InOut
import Normalisierungsfunktionen


#Funktion zur Durchfuehrung der spezifischen Extraktion und Speicherung der Daten
def extractionOfFeatures(parameter, y):

    feature = parameter.operationDictionary[parameter.operations](y, parameter)
    return feature


#Extraktionsfunktion
def extract(inputFolder, outputFolder, parameter, stringList):

    parameter.setOperations(stringList)
    parameter.checkIntegrity()
    audioList = InOut.listAudios(inputFolder)
    FolderOperations.createOutPutFolders(outputFolder, parameter)
    #normalizationArray = np.empty([parameter.normalizationDictionary[parameter.operations], 1])
    normalizationArray = np.empty([parameter.normalizationDictionary[parameter.operations] +1 , 1])
    timeframeSum = 0

    for file in audioList:
        y, sr, filename = InOut.readInAudio(inputFolder, file)
        feature = extractionOfFeatures(parameter, y)
        FolderOperations.saveFeatures(feature, parameter, outputFolder, filename)
        normalizationArray, timeframeSum = Normalisierungsfunktionen.addFeatureToNormalization(feature, normalizationArray, timeframeSum)
    Normalisierungsfunktionen.saveNormalizationArray(normalizationArray, outputFolder, parameter)
    #Normalisierungsfunktionen.saveTimeframeSum(timeframeSum, outputFolder, parameter)

    return None




### Klasse: Normalisierungsklasse
### normalisierungsbean. 2 eigenschaften: Timeframes, Featurewerte.
### featurewerte

### Normlisierungsklasse.aktualisiereWerte



