class Parameter(object):
    def __init__(self, n_fft=512, win_length=40, hop_length=40, n_mels=40, power=2,
                     mfccs=20, freqAxis='linear', dispRef=512):

        self.n_fft = n_fft
        #values for win_length and hop_length are directly converted from [ms] to samples
        #22050 is the default sampling rate of librosa's file import
        self.win_length = int(win_length * 0.001 * 22050)
        self.hop_length = int(hop_length * 0.001 * 22050)
        self.n_mels = n_mels
        self.power = power
        self.mfccs = mfccs
        self.freqAxis = freqAxis
        self.dispRef = dispRef

    #
    def checkIntegrity(self):
        print("checking n_fft >= win_length")
        if self.win_length > self.n_fft:
            self.n_fft = self.win_length
        else:
            self.n_fft = self.n_fft
#_______________ only for debugging__start__
    def sayHello(self):
        print("succesful method call")

    def printNFFT(self):
        print(self.n_fft)
#_______________ only for debugging__end__
