import numpy as np

#Funktion um Normalisierungsvektor anzulegen
def createMFCCMatrix(audioList, parameter):
    numberOfFiles = len(audioList)
    numberOfFeatures = parameter.mfccs
    MFCCMatrix = np.empty((numberOfFeatures, numberOfFiles))
    return MFCCMatrix

#Funktion um MFCCs fuer Normalisierung zu verwenden
def addMFCCsToMFCCMatrix(MFCCMatrix, F, audioList, file, parameter):
    index = audioList.index(file)
    numberMFCCs = parameter.mfccs
    for x in range(0, numberMFCCs):
        MFCCMatrix[index][x] = F[x][0]
    return MFCCMatrix

#Funktion um Normalisierungsfaktoren aus MFCC Matrix zu berechnen
def calcNormalizationFactor(MFCCMatrix, outputFolder):
    numberOfFeatures, numberOfFiles = MFCCMatrix.shape
    normalizationVector = np.empty((numberOfFeatures, 1))
    for i in range(0, numberOfFeatures):
        normalizationVector[i][0] = np.sum(MFCCMatrix[i]) / numberOfFiles
    datafile = open(outputFolder + '_Normalisierungsfaktoren_MFCCS', 'wb')
    np.save(datafile, normalizationVector)
    return None