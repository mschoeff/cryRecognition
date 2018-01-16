import ParameterCheck
import getOperations
import SpectralFeatures
import Displayfunctions

class Parameter(object):

    def __init__(self, n_fft=512, win_length=40, hop_length=40, window = "hann", symmetry = False, n_mels=40, power=2,
                     mfccs=20, freqAxis='linear', dispRef=512, operations = "SPEKTRUM"):

        self.n_fft = n_fft
        self.win_length = win_length
        self.hop_length = hop_length
        self.window = window
        self.symmetry = symmetry
        self.n_mels = n_mels
        self.power = power
        self.mfccs = mfccs
        self.freqAxis = freqAxis
        self.dispRef = dispRef
        self.operations = operations

        # self.operationDictionary = {
        #     "SPEKTRUM": computeSpectralFeatures.computeSpectrum,
        #     "MELSPEKTRUM" : computeSpectralFeatures.computeMelSpectrum,
        #     "MFCCS": computeSpectralFeatures.computeMFCC
        # }

        self.normalizationDictionary = {
            "SPEKTRUM": 1 + self.n_fft / 2,
            "MELSPEKTRUM": self.n_mels,
            "MFCCS": self.mfccs
        }
        # self.displayDictionary = {
        #     "AUDIO" : Displayfunktionen.displayAudio,
        #     "SPEKTRUM" : Displayfunktionen.displaySpectrogram,
        #     "MELSPEKTRUM" : Displayfunktionen.displayMelSpectrogram
        # }

    def checkIntegrity(self):
        self.win_length = ParameterCheck.calcSamples(self.win_length, 22050)
        self.hop_length = ParameterCheck.calcSamples(self.hop_length, 22050)
        self.n_fft = ParameterCheck.checkFFTSamples(self.n_fft, self.win_length)

    def setOperations(self, input):
        self.operations = getOperations.capitalizeStrings(input)

    def numDisplayOperations(self):
        return len(self.operations)
