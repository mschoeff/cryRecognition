import librosa
import numpy as np

def computeSpectrum(y, parameter):
    S = librosa.stft(y=y,n_fft=parameter.n_fft, hop_length=parameter.hop_length, win_length=parameter.win_length)
    S = (np.abs(S) ** 2)/parameter.n_fft
    return S

def computeMelSpectrum(y, parameter):
    S = computeSpectrum(y, parameter)
    M = librosa.feature.melspectrogram(S=S, power = parameter.power, n_mels = parameter.power)
    return M

def computeMFCC(y, parameter):
    M = computeMelSpectrum(y, parameter)
    F = librosa.feature.mfcc(S = M, n_mfcc= parameter.n_mfccs)
    return F
