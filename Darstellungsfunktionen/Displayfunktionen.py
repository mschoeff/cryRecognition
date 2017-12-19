import librosa.display as libdisp
import matplotlib.pyplot as mp
import numpy as np
from InOut import *
from ParameterCheck import *
from getOperations import *
from computeSpectralFeatures import *
#Funktion um Anzahl der Plots zu berechnen
def numberOfPlots(displayOperations):
    numPlots = 0
    if displayOperations.dispAudio:
        numPlots += 1
    if displayOperations.dispSpec:
        numPlots += 1
    if displayOperations.dispMelSpec:
        numPlots += 1
    return  numPlots

#Funktion um Audiodatei darzustellen
def displayAudio(numPlots, y, sr, filename):
    mp.subplot(numPlots, 1, 1)
    mp.title(filename)
    time = np.linspace(0, len(y)/sr, len(y))
    mp.plot(time, y)
    return None

#Funktion um Spektrogramm darzustellen
def displaySpectrogram(pr, numPlots, y, sr, filename, displayOperations):
    D = computeSpectrum(y, pr)
    if displayOperations.dispAudio:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(D, cmap='gray_r', y_axis=pr.freqAxis)#, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title(filename + ' - ' + pr.freqAxis + ' power spectrogram')
    return None

#Funktion um Mel-Spektrogramm darzustellen
def displayMelSpectrogram(pr, numPlots, y, sr, filename, displayOperations):
    M = computeMelSpectrum(y, pr)
    if displayOperations.dispSpec and displayOperations.dispAudio:
        mp.subplot(numPlots, 1, 3)
    elif displayOperations.dispSpec and displayOperations.dispAudio == False:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(M, cmap='gray_r', y_axis='mel') #, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title(filename + ' - ' + 'Mel' + ' power spectrogram')
    return None


#Darstellungsfunktion
def display(filepath, displayParameter, stringList):


    displayFunctions, parameter = checkDisplayParameterIntegrity(stringList, displayParameter)

    operationString = capitalizeStrings(stringList)
    displayFunctions = getDisplayOperations(operationString)

    y, sr, file = readInAudioDirectly(filepath)

    if displayFunctions.dispAudio:
        displayAudio(numberOfPlots(displayFunctions), y, sr, file)
    if displayFunctions.dispSpec:
        displaySpectrogram(displayParameter, numberOfPlots(displayFunctions), y, sr, file, displayFunctions)
    if displayFunctions.dispMelSpec:
        displayMelSpectrogram(displayParameter, numberOfPlots(displayFunctions), y, sr, file,
                              displayFunctions)
    mp.show()
    return None
