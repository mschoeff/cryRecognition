import numpy as np
import FolderOperations
import InOut
import Normalisierungsfunktionen
import SpectralFeatures
import normalizer

#Dictionary providing appropriate function for specific operation
operationDictionary = {
    "SPEKTRUM": SpectralFeatures.computeSpectrum,
    "MELSPEKTRUM": SpectralFeatures.computeMelSpectrum,
    "MFCCS": SpectralFeatures.computeMFCC
}

#Funktion zur Durchfuehrung der spezifischen Extraktion und Speicherung der Daten
def extractionOfFeatures(parameter, y):

    feature = operationDictionary[parameter.operations](y, parameter)
    return feature

#Extraktionsfunktion
def extract(inputFolder, outputFolder, parameter, stringList):

    parameter.setOperations(stringList)
    parameter.checkIntegrity()
    audioList = InOut.listAudios(inputFolder)
    FolderOperations.createOutPutFolders(outputFolder, parameter)

    Normalizer = normalizer.Normalizer(parameter)

    for file in audioList:

        y, sr, filename = InOut.readInAudio(inputFolder, file)
        feature = extractionOfFeatures(parameter, y)
        FolderOperations.saveFeatures(feature, parameter, outputFolder, filename)
        Normalizer.addFeature(feature)
    Normalizer.calcArithMeansAndStdDevs()
    #print(Normalizer.arithMeans)
    Normalizer.saveArithMeansAndStdDevs(parameter, outputFolder)

    return None




### Klasse: Normalisierungsklasse
### normalisierungsbean. 2 eigenschaften: Timeframes, Featurewerte.
### featurewerte

### Normlisierungsklasse.aktualisiereWerte



