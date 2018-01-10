import numpy as np


def addFeatureToNormalization(feature, normalizationArray, timeFrames):
    featureValues, featureFrames = feature.shape
    timeFrames += featureFrames
    for singleFeatureValue in range(featureValues):
        normalizationArray[singleFeatureValue][0] += sum(feature[singleFeatureValue])
    return (normalizationArray, timeFrames)

def saveNormalizationArray(normalizationArray, outputFolder, parameter):
    datafile = open(outputFolder + '/' + parameter.operations + '-Daten/' + 'Normalisierungsfaktoren_' + parameter.operations, 'wb')
    np.save(datafile, normalizationArray)
    return None

def saveTimeframeSum(timeframeSum, outputFolder, parameter):
    datafile = open(outputFolder + '/' + parameter.operations + '-Daten/' + 'TimeframeSum_' + parameter.operations, 'wb')
    np.save(datafile, timeframeSum)
    return None