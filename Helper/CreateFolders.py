import os

#Funktion um einzelnen Ordner zu erstellen
def createSingleFolder(path, name):
    if not os.path.exists(path + "/" + name):
        os.makedirs(path + "/" + name)
    return None

#Funktion um Zielordner fuer Speicherung zu erstellen
def createOutPutFolders(outputPath, parameter):
    # if extractionFunctions.saveSpec:
    #     createSingleFolder(outputPath, "STFT_Data")
    # if extractionFunctions.saveMelSpec:
    #     createSingleFolder(outputPath, "MEL_Data")
    # if extractionFunctions.saveMFCCs:
    #     createSingleFolder(outputPath, "MFCC_Data")
    createSingleFolder(outputPath, parameter.operations + "-Daten")
    return None
