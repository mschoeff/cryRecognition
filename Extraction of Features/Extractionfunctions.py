import FolderOperations
import InOut
import SpectralFeatures
import normalizer
import UnitTest

#Dictionary providing appropriate function for specific operation
operationDictionary = {
    "SPEKTRUM": SpectralFeatures.computePowerSpectrogram,
    "MELSPEKTRUM": SpectralFeatures.computeMelSpectrum,
    "MFCCS": SpectralFeatures.computeMFCC
}

#Function that calls appropriate extraction function based on operation to be performed
def extractionOfFeatures(parameter, y):

    feature = operationDictionary[parameter.operations](y, parameter)
    return feature

#Extractionfunction
def extract(inputFolder, outputFolder, parameter, stringList):

    parameter.setOperations(stringList)
    parameter.checkIntegrity()
    audioList = InOut.listAudios(inputFolder)
    FolderOperations.createOutPutFolders(outputFolder, parameter)

    Normalizer = normalizer.Normalizer(parameter)

    for file in audioList:

        y, sr, filename = InOut.readInAudio(inputFolder, file)
        feature = extractionOfFeatures(parameter, y)
        FolderOperations.saveFeatures(feature, parameter, outputFolder, filename)
        Normalizer.addFeature(feature)
    #
    #A, B, check = UnitTest.testMFCCS(y, parameter)
    #print(check)
    Normalizer.calcArithMeansAndStdDevs()
    Normalizer.saveArithMeansAndStdDevs(parameter, outputFolder)

    return None




