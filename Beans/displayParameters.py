class displayParameter(object):
    def __init__(self, n_fft=512, win_length=40, hop_length=40, freqAxis='linear', dispRef=512, n_mels=40, power=2,
                     mfccs=20):
        self.n_fft = n_fft
        self.win_length = win_length
        self.hop_length = hop_length
        self.freqAxis = freqAxis
        self.dispRef = dispRef
        self.n_mels = n_mels
        self.power = power
        self.mfccs = mfccs

