import normalizer
import numpy as np

#"dataset" containing information in the same format of features
testFeature1 = np.array([[1., 2., 3., 4., 5., 6., 7., 8., 9., 10.], [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]])
testFeature2 = np.array([[2, 2., 2.], [4., 4., 4.]])
testFeature3 = np.array([[4., 5., 6.], [7., 8., 9.]])

#slimmed version of Parameter class containing only the relevant parameters for the creation of the normalizer-object
#mfccs is used as operation-mode and set to 2 for clarity and simplicity
class Paras(object):
    def __init__(self, n_fft=512, n_mels=40, mfccs=2, operations = "MFCCS"):
        self.n_fft = n_fft
        self.n_mels = n_mels
        self.mfccs = mfccs
        self.operations = operations
        self.normalization_Dictionary = {
            "SPEKTRUM": 1 + self.n_fft / 2,
            "MELSPEKTRUM": self.n_mels,
            "MFCCS": self.mfccs
        }

Parameter = Paras()
Normalizer = normalizer.Normalizer(Parameter)

#print(Normalizer)

Normalizer.add_Feature(testFeature1)
Normalizer.add_Feature(testFeature2)
Normalizer.add_Feature(testFeature3)

Normalizer.calc_Arith_Means()
print(Normalizer.arith_Means)
#print(Normalizer.stdDevs)