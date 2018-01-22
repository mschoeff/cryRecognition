import numpy as np
import FeatureDimensions

class Normalizer(object):

    __instance = None

    #Dictionary providing appropriate size for normalization Array for specific feature
    normalizationDictionary = {
            "SPEKTRUM": FeatureDimensions.stftSize,
            "MELSPEKTRUM": FeatureDimensions.melSize,
            "MFCCS": FeatureDimensions.mfccSize
    }
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

        self.features = np.empty([self.normalizationDictionary[parameter.operations](parameter) + 1 , 2])
        self.timeframeSum = 0
        self.arithMeans = 0
        self.stdDevs = 0

    def addFeature(self, feature):
        featureValues, featureFrames = feature.shape
        self.timeframeSum += featureFrames
        for singleFeatureValue in range(featureValues):
            self.features[singleFeatureValue][0] += sum(feature[singleFeatureValue])
            self.features[singleFeatureValue][1] += np.std(feature[singleFeatureValue]) * featureFrames
        self.features[featureValues][0] = self.timeframeSum

    def calcArithMeansAndStdDevs(self):
        x, y = self.features.shape
        self.arithMeans = np.empty([x])
        self.stdDevs = np.empty([x])
        for singleFeature in range(x):
            self.arithMeans[singleFeature] = self.features[singleFeature][0] / self.features[x-1][0]
            self.stdDevs[singleFeature] = self.features[singleFeature][1] / self.features[x-1][0]

    def saveArithMeansAndStdDevs(self, parameter, outputFolder):
        datafile = open(outputFolder + '/' + parameter.operations + '-Daten/' + 'Normalisierungsfaktoren_' + parameter.operations, 'wb')
        np.save(datafile, (self.arithMeans, self.stdDevs))
        return None
