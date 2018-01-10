import ParameterCheck
import getOperations
import computeSpectralFeatures
import Displayfunktionen

class Parameter(object):

    def __init__(self, n_fft=512, win_length=40, hop_length=40, n_mels=40, power=2,
                     mfccs=20, freqAxis='linear', dispRef=512, operations = "SPEKTRUM"):

        # def convertMilliSecondsToSamples(ms, sr):
        #     samples = int(ms * 0.001 * sr)  # Faktor 0.001, da Zeit [ms]
        #     return samples

        #self.n_fft = n_fft
        self.n_fft = ParameterCheck.checkFFTSamples(n_fft, win_length, 22050)

        #values for win_length and hop_length are directly converted from [ms] to samples
        #22050 is the default sampling rate of librosa's file import
        self.win_length = ParameterCheck.calcSamples(win_length, 22050)
        self.hop_length = ParameterCheck.calcSamples(hop_length, 22050)
        self.n_mels = n_mels
        self.power = power
        self.mfccs = mfccs
        self.freqAxis = freqAxis
        self.dispRef = dispRef
        self.operations = operations
        self.operationDictionary = {
            "SPEKTRUM": computeSpectralFeatures.computeSpectrum,
            "MELSPEKTRUM" : computeSpectralFeatures.computeMelSpectrum,
            "MFCCS": computeSpectralFeatures.computeMFCC
        }
        self.normalizationDictionary = {
            "SPEKTRUM": 1 + self.n_fft / 2,
            "MELSPEKTRUM": self.n_mels,
            "MFCCS": self.mfccs
        }
        self.displayDictionary = {
            "AUDIO" : Displayfunktionen.displayAudio,
            "SPEKTRUM" : Displayfunktionen.displaySpectrogram,
            "MELSPEKTRUM" : Displayfunktionen.displayMelSpectrogram
        }

    def checkIntegrity(self):
        print("checking n_fft >= win_length")
        if self.win_length > self.n_fft:
            self.n_fft = self.win_length
        else:
            self.n_fft = self.n_fft

    def setOperations(self, input):
        self.operations = getOperations.capitalizeStrings(input)

    def numDisplayOperations(self):
        return len(self.operations)

#_______________ only for debugging__start__
    def sayHello(self):
        print("succesful method call")

    def printNFFT(self):
        print(self.n_fft)
#_______________ only for debugging__end__
