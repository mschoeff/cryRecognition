import Parameter_Check
import get_Operations

class Parameter(object):

    def __init__(self, n_fft=512, win_length=40, hop_length=40, window = "hann", symmetry = False, n_mels=40, power=2,
                 mfccs=20, frequency_Axis='linear', disp_Ref=512, operations ="SPEKTRUM"):

        self.n_fft = n_fft
        self.win_length = win_length
        self.hop_length = hop_length
        self.window = window
        self.symmetry = symmetry
        self.n_mels = n_mels
        self.power = power
        self.mfccs = mfccs
        self.frequency_Axis = frequency_Axis
        self.display_Reference = disp_Ref
        self.operations = operations
        self.normalization_Dictionary = {
            "SPEKTRUM": 1 + self.n_fft / 2,
            "MELSPEKTRUM": self.n_mels,
            "MFCCS": self.mfccs
        }
        self.display_Dictionary = {
            "SPEKTRUM": self.frequency_Axis,
            "MELSPEKTRUM": 'mel',
            "DB_SPEKTRUM": self.frequency_Axis
        }


    def check_Integrity(self):
        self.win_length = Parameter_Check.calc_Samples(self.win_length, 22050)
        self.hop_length = Parameter_Check.calc_Samples(self.hop_length, 22050)
        self.n_fft = Parameter_Check.check_FFT_Samples(self.n_fft, self.win_length)

    def set_Operations(self, input):
        self.operations = get_Operations.capitalize_Strings(input)

    def number_Display_Operations(self):
        return len(self.operations)
