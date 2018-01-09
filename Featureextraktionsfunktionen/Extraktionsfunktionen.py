import numpy as np
from CreateFolders import *
from InOut import *
from ParameterCheck import *
from getOperations import *
from computeSpectralFeatures import *
from Normalisierungsfunktionen import *
import parameter
#Funktion zur Durchfuehrung der spezifischen Extraktion und Speicherung der Daten
def extractionOfFeatures(extractionFunctions, pr, inputFolder, file):
    y, sr, filename = readInAudio(inputFolder, file)
    print(len(y))
    #S, M, F = 0
    #FactoryPattern googeln
    if extractionFunctions.saveSpec:
        S = computeSpectrum(y, pr)

    if extractionFunctions.saveMelSpec:
        M = computeMelSpectrum(y, pr)

    if extractionFunctions.saveMFCCs:
        F = computeMFCC(y, pr)

    return (S, M, F, filename)

#Funktion zur Abspeicherung der extrahierten Features
def saveFeatures(S, M, F, extractionFunctions, outputFolder, filename):

    if extractionFunctions.saveSpec:
        datafile = open(outputFolder + '/STFT_Data/' + filename + '_STFT_data', 'wb')
        np.save(datafile, S)

    if extractionFunctions.saveMelSpec:
        datafile = open(outputFolder + '/MEL_Data/' + filename + '_MEL_data', 'wb')
        np.save(datafile, M)

    if extractionFunctions.saveMFCCs:
        datafile = open(outputFolder + '/MFCC_Data/' + filename + '_MFCCs', 'wb')
        np.save(datafile, F)

    return None


#Extraktionsfunktion
def extract(inputFolder, outputFolder, parameter, stringList):

    #extractionFunctions, extrparameter = checkExtractionParameterIntegrity(stringList, parameter)
    #extractionFunctions = checkExtractionParameterIntegrity(stringList, parameter)

    extractionFunctions = getExtractionOperations(capitalizeStrings(stringList))
    print (capitalizeStrings(stringList))
    parameter.checkIntegrity()

    audioList = listAudios(inputFolder)
    createOutPutFolders(outputFolder, extractionFunctions)
    MFCCMatrix = createMFCCMatrix(audioList, parameter)
    for file in audioList:
        S, M, F, filename = extractionOfFeatures(extractionFunctions, parameter, inputFolder, file)
        #addMFCCsToMFCCMatrix(MFCCMatrix, F, audioList, file, parameter)
        saveFeatures(S, M, F, extractionFunctions, outputFolder, filename)
    calcNormalizationFactor(MFCCMatrix, outputFolder)

    return None
