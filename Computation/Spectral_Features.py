import librosa
import numpy as np

def compute_Power_Spectrogram(y, parameter):
    #S = librosa.stft(y=y,n_fft=parameter.n_fft, hop_length=parameter.hop_length, win_length=parameter.win_length,
    #                 window = parameter.window, center = parameter.symmetry)
    #S = (np.abs(S) ** 2)/parameter.n_fft
    #S = 20 * np.log10((abs(S)**2)/parameter.dispRef)
    #S = librosa.amplitude_to_db(S, ref=1)#parameter.n_fft)

    S = np.abs(librosa.stft(y=y, n_fft=parameter.n_fft, hop_length=parameter.hop_length))
    P = S ** parameter.power
    return P

def compute_Mel_Spectrum(y, parameter):
    #S = computeSpectrum(y, parameter)
    #M = librosa.feature.melspectrogram(S=S, power = parameter.power, n_mels = parameter.n_mels)
    P = compute_Power_Spectrogram(y, parameter)
    M = librosa.feature.melspectrogram(S=P, n_mels=parameter.n_mels)
    return M

def compute_MFCC(y, parameter):
    M = compute_Mel_Spectrum(y, parameter)
    M = librosa.power_to_db(M, ref=1.0)
    F = librosa.feature.mfcc(S=M, n_mfcc=parameter.mfccs)
    return F


def compute_Normalized_Log_Spectrogram(y, parameter):
    P = compute_Power_Spectrogram(y, parameter)
    P_db = librosa.power_to_db(P, ref=parameter.n_fft )
    return P_db

