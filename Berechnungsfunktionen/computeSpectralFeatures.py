import librosa
import numpy as np

def computeSpectrum(y, parameter):
    S = librosa.stft(y=y,n_fft=parameter.n_fft, hop_length=parameter.hop_length, win_length=parameter.win_length,
                     window = parameter.window, center = parameter.symmetry)
    #S = (np.abs(S) ** 2)/parameter.n_fft
    #S = 20 * np.log10((abs(S)**2)/parameter.dispRef)
    S = librosa.amplitude_to_db(S, ref=parameter.n_fft)
    return S

def computeMelSpectrum(y, parameter):
    S = computeSpectrum(y, parameter)
    M = librosa.feature.melspectrogram(S=S, power = parameter.power, n_mels = parameter.n_mels)
    return M

def computeMFCC(y, parameter):
    M = computeMelSpectrum(y, parameter)
    F = librosa.feature.mfcc(S = M, n_mfcc= parameter.mfccs)
    return F
