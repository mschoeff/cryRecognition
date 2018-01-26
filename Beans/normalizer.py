import numpy as np

class Normalizer(object):

    __instance = None

    # @staticmethod
    # def getInstance():
    #     if Normalizer.__instance is None:
    #         Normalizer()
    #     return Normalizer.__instance

    def __init__(self, parameter):
        if Normalizer.__instance is not None:
            raise Exception("Normalizer is Singleton Class")
        else:
            Normalizer.__instance = self

        #for each new attribute to be "normalized": feature_Sum array dim [+1,...]
        self.feature_Sum = np.empty([1, self.normalization_Dictionary[parameter.operations](self, parameter)])
        self.timeframe_Sum = 0
        self.arith_Means = 0
        ### Standard Deviation to be implemented
        #self.stdDevs = 0

    def add_Feature(self, feature):
        feature_Values, feature_Frames = feature.shape
        self.timeframe_Sum += feature_Frames
        self.feature_Sum[0][0:feature_Values] += np.sum(feature, axis = 1)
        #self.featureSum[1][0:featureValues] += np.dot(np.std(feature, axis = 1), featureFrames)
        return None

    def calc_Arith_Means(self):
        x, y = self.feature_Sum.shape
        self.arith_Means = np.empty([y])
        #self.stdDevs = np.empty([y])

        self.arith_Means[:y] = np.divide(self.feature_Sum[0][:y], self.timeframe_Sum)
        #self.stdDevs[:y] = np.divide(self.featureSum[1][:y], self.timeframeSum)

    def save_Arith_Means(self, parameter, output_Folder):
        datafile = open(output_Folder + '/' + parameter.operations + '-Daten/' + 'Normalisierungsfaktoren_' + parameter.operations, 'wb')
        np.save(datafile, self.arith_Means) #, self.stdDevs))
        return None

    def stftSize(self, parameter):
        return 1 + parameter.n_fft / 2

    def melSize(self, parameter):
        return parameter.n_mels

    def mfccSize(self, parameter):
        return parameter.mfccs

    #Dictionary providing appropriate size for normalization Array for specific feature
    normalization_Dictionary = {
            "SPEKTRUM": stftSize,
            "MELSPEKTRUM": melSize,
            "MFCCS": mfccSize
    }