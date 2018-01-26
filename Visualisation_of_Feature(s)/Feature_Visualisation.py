import matplotlib.pyplot as mp
import numpy as np
import Spectral_Features
import librosa.display as libdisp


def displayAudio(y, sr, filename, parameter):
    numPlots = len(parameter.operations)
    mp.subplot(numPlots, 1, 1)
    mp.title(filename)
    time = np.linspace(0, len(y)/sr, len(y))
    mp.plot(time, y)
    return None

def displaySpectrogram(y, sr, filename, parameter):
    #sr and filename are defined in head of function to match the scheme of displayAudio -> unified calling is possible
    numPlots = len(parameter.operations)
    D = Spectral_Features.compute_Power_Spectrogram(y, parameter)
    if "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(D, cmap='gray_r', y_axis=parameter.freqAxis)#, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title(parameter.freqAxis + ' power spectrogram')
    return None

def displayMelSpectrogram(y, sr, filename, parameter):
    #sr and filename are defined in head of function to match the scheme of displayAudio -> unified calling is possible
    numPlots = len(parameter.operations)
    M = Spectral_Features.compute_Mel_Spectrum(y, parameter)
    if "SPEKTRUM" in parameter.operations and "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 3)
    elif "SPEKTRUM" in parameter.operations or "AUDIO" in parameter.operations:
        mp.subplot(numPlots, 1, 2)
    else:
        mp.subplot(numPlots, 1, 1)
    libdisp.specshow(M, cmap='gray_r', y_axis='mel') #, x_axis='time'
    mp.colorbar(orientation='horizontal', format='%+2.0f dB')
    mp.title('Mel' + ' power spectrogram')
    return None

def displayDBSpectrogram(y, sr, filename, parameter):
    #sr and filename are defined in head of function to match the scheme of displayAudio -> unified calling is possible
    numPlots = len(parameter.operations)
    D = Spectral_Features.compute_Normalized_Log_Spectrogram(y, parameter)
    mp.subplot(numPlots, 1, numPlots)
    libdisp.specshow(D, cmap='gray_r', y_axis=parameter.freqAxis)#, x_axis='time'
    mp.colorbar(orientation='horizontal')#, format='%+2.0f dB')
    mp.title(parameter.freqAxis + ' DB spectrogram')
    return None
