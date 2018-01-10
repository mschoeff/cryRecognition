import librosa.display as libdisp
import matplotlib.pyplot as mp
import numpy as np
import InOut
import computeSpectralFeatures

#Funktion um Audiodatei darzustellen
def displayAudio(y, sr, filename, parameter):
    numPlots = len(parameter.operations)
    mp.subplot(numPlots, 1, 1)
    mp.title(filename)
    time = np.linspace(0, len(y)/sr, len(y))
    mp.plot(time, y)
    return None

#Funktion um Spektrogramm darzustellen
def displaySpectrogram(y, sr, filename, parameter):
    numPlots = len(parameter.operations)
    D = computeSpectralFeatures.computeSpectrum(y, parameter)
    if "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(D, cmap='gray_r', y_axis=parameter.freqAxis)#, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title(filename + ' - ' + parameter.freqAxis + ' power spectrogram')
    return None

#Funktion um Mel-Spektrogramm darzustellen
def displayMelSpectrogram(y, sr, filename, parameter):
    numPlots = len(parameter.operations)
    M = computeSpectralFeatures.computeMelSpectrum(y, parameter)
    if "SPEKTRUM" in parameter.operations and "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 3)
    elif "SPEKTRUM" in parameter.operations or "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(M, cmap='gray_r', y_axis='mel') #, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title(filename + ' - ' + 'Mel' + ' power spectrogram')
    return None


#Darstellungsfunktion
def display(filepath, displayParameter, stringList):

    displayParameter.setOperations(stringList)
    y, sr, file = InOut.readInAudioDirectly(filepath)
    [displayParameter.displayDictionary[displayOperation](y, sr, file, displayParameter) for displayOperation in displayParameter.operations]
    mp.show()
    return None
