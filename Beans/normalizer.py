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

        self.featureSum = np.empty([2, self.normalizationDictionary[parameter.operations](self, parameter)])
        self.timeframeSum = 0
        self.arithMeans = 0
        self.stdDevs = 0

    def addFeature(self, feature):
        featureValues, featureFrames = feature.shape
        self.timeframeSum += featureFrames
        self.featureSum[0][0:featureValues] += np.sum(feature, axis = 1)
        self.featureSum[1][0:featureValues] += np.std(feature, axis = 1)
        # for singleFeatureValue in range(featureValues):
        #     self.features[singleFeatureValue][0] += sum(feature[singleFeatureValue])
        #     self.features[singleFeatureValue][1] += np.std(feature[singleFeatureValue]) * featureFrames
        #self.features[featureValues][0] = self.timeframeSum

    def calcArithMeansAndStdDevs(self):
        x, y = self.featureSum.shape
        self.arithMeans = np.empty([y])
        self.stdDevs = np.empty([y])

        self.arithMeans[:y] = np.divide(self.featureSum[0][:y], self.timeframeSum)
        self.stdDevs[:y] = np.divide(self.featureSum[1][:y], self.timeframeSum)
        # for singleFeature in range(y):
        #     self.arithMeans[singleFeature] = self.featureSum[0][singleFeature] / self.timeframeSum #self.features[x-1][0]
        #     self.stdDevs[singleFeature] = self.featureSum[1][singleFeature] / self.timeframeSum #self.features[x-1][0]

    def saveArithMeansAndStdDevs(self, parameter, outputFolder):
        datafile = open(outputFolder + '/' + parameter.operations + '-Daten/' + 'Normalisierungsfaktoren_' + parameter.operations, 'wb')
        np.save(datafile, (self.arithMeans, self.stdDevs))
        return None

    def stftSize(self, parameter):
        return 1 + parameter.n_fft / 2

    def melSize(self, parameter):
        return parameter.n_mels

    def mfccSize(self, parameter):
        return parameter.mfccs

    #Dictionary providing appropriate size for normalization Array for specific feature
    normalizationDictionary = {
            "SPEKTRUM": stftSize,
            "MELSPEKTRUM": melSize,
            "MFCCS": mfccSize
    }