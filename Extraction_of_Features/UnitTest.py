###Unit Test MFCC
import Spectral_Features
import librosa
import numpy as np

def testMFCCS(y, parameter):



    #A = SpectralFeatures.computeMFCC(y, parameter)
    A = librosa.feature.mfcc(y,n_mfcc = parameter.mfccs, n_fft = parameter.n_fft,
                             hop_length = parameter.hop_length, power = parameter.power)
                             # ,
                             # win_length = parameter.win_length, window = parameter.window,
                             # power = parameter.power, center = parameter.symmetry)
    B = librosaPipeline(y, parameter)
    F = ownPipeline(y, parameter)


    if np.array_equal(A, B):
        check = True
    else:
        check = False

    return (A, B, check)

def librosaPipeline(y, parameter):

    return Spectral_Features.compute_MFCC(y, parameter)

    #S = np.abs(librosa.stft(y = y, n_fft = parameter.n_fft, hop_length = parameter.hop_length))
    #P = S**parameter.power
    #M = librosa.feature.melspectrogram(S=P, n_mels = parameter.n_mels)
    #M = librosa.power_to_db(M, ref=1.0)
    #F = librosa.feature.mfcc(S=M, n_mfcc=parameter.mfccs)

    #mel_basis = librosa.filters.mel(22050, parameter.n_fft)
    #MEL = np.dot(mel_basis, S)
    #P = librosa.power_to_db(MEL)
    #M = np.dot(librosa.filters.dct(parameter.mfccs, P.shape[0]), P)
    #return F

def ownPipeline(y, parameter):
    S = librosa.stft(y=y,n_fft=parameter.n_fft, hop_length=parameter.hop_length, win_length=parameter.win_length,
                     window = parameter.window, center = parameter.symmetry)
    S = librosa.amplitude_to_db(S, ref = 1.0)
    M = librosa.feature.melspectrogram(S = S, power = parameter.power, n_mels = parameter.n_mels)
    F = librosa.feature.mfcc(S = M, n_mfcc = parameter.mfccs)
    return F