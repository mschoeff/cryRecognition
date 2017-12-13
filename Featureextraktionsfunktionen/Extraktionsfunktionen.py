import numpy as np
from CreateFolders import *
from InOut import *
from ParameterCheck import *
from getOperations import *

#Funktion zur Durchfuehrung der spezifischen Extraktion und Speicherung der Daten
def extractAndSave(extractionFunctions, pr, inputFolder, outputFolder, file):
    y, sr, filename = readInAudio(inputFolder, file)

    #checkParamterIntegrity()
    #hoplength

    #FactoryPattern googeln
    if extractionFunctions.saveSpec:
        S = librosa.stft(y, checkFFTSamples(pr.n_fft, pr.win_length, sr), calcSamples(pr.hop_length, sr),
                         calcSamples(pr.win_length, sr))
        #datafile = open(outputFolder + '/STFT_Data/' + filename + '_STFT_data', 'wb')
        #np.save(datafile, S)

    if extractionFunctions.saveMelSpec:
        S = librosa.stft(y, checkFFTSamples(pr.n_fft, pr.win_length, sr), calcSamples(pr.hop_length, sr),
                         calcSamples(pr.win_length, sr))
        M = librosa.feature.melspectrogram(S=S, n_fft=checkFFTSamples(pr.n_fft, pr.win_length, sr),
                                           hop_length=calcSamples(pr.hop_length,sr), power=pr.power, n_mels = pr.n_mels)
        #datafile = open(outputFolder + '/MEL_Data/' + filename + '_MEL_data', 'wb')
        #np.save(datafile, M)

    if extractionFunctions.saveMFCCs:
        F = librosa.feature.mfcc(y=y, sr=sr, n_fft=checkFFTSamples(pr.n_fft, pr.win_length, sr),
                                 hop_length=calcSamples(pr.hop_length,sr), power=pr.power, n_mfcc = pr.mfccs)
        #datafile = open(outputFolder + '/MFCC_Data/' + filename + '_MFCCs', 'wb')
        #np.save(datafile, F)

    #save(MFCC)
    return None

#Extraktionsfunktion
def extract(inputFolder, outputFolder, parameter, stringList):
    #anmerkung spaeter
    #checkInputParameterIntegry(stringList)

    operationString = capitalizeStrings(stringList)
    extractionFunctions = getExtractionOperations(operationString)
    audioList = listAudios(listFiles(inputFolder))
    createOutPutFolders(outputFolder, extractionFunctions)

    [extractAndSave(extractionFunctions, parameter, inputFolder, outputFolder, file) for file in audioList]

    return None
