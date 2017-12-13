import librosa.display as libdisp
import matplotlib.pyplot as mp
import numpy as np
from InOut import *
from ParameterCheck import *
from getOperations import *

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
    S = librosa.stft(y, checkFFTSamples(pr.n_fft, pr.win_length, sr), hop_length=calcSamples(pr.hop_length,sr),
                     win_length=calcSamples(pr.win_length,sr))
    #D = librosa.amplitude_to_db(S, ref=pr.dispRef)
    D = (S ** 2) / pr.n_fft
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
    S = librosa.stft(y, checkFFTSamples(pr.n_fft, pr.win_length, sr), hop_length=calcSamples(pr.hop_length,sr),
                     win_length=calcSamples(pr.win_length,sr))
    S = (S ** 2) / pr.n_fft
    M = librosa.feature.melspectrogram(S=S, n_fft=checkFFTSamples(pr.n_fft, pr.win_length, sr),
                                       hop_length=calcSamples(pr.hop_length,sr), power=pr.power, n_mels = pr.n_mels)
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
