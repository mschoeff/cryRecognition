from extractOperations import extractOperations
from displayOperations import displayOperations
import types


#Funktion um eingegebene Strings zu "capitalizen"
def capitalizeStrings(input):
    #output = 1
    if isinstance(input, types.StringType):
        output = input.upper()
    if isinstance(input, types.ListType):
        output = [s.upper() for s in input]
    return output

#Funktion um durchzufuehrende Extraktions-Operationen zu bestimmen
def getExtractionOperations(operationString):

    extractionFunctions = extractOperations(saveSpec = False, saveMelSpec = False, saveMFCCs = False)

    if "SPEKTRUM" in operationString:
        extractionFunctions.saveSpec = True
    if "MELSPEKTRUM" in operationString:
        extractionFunctions.saveMelSpec = True
    if "MFCCS" in operationString:
        extractionFunctions.saveMFCCs = True

    return extractionFunctions

#Funktion um durchzufuehrende Darstellungs-Operationen zu bestimmen
def getDisplayOperations(operationString):

    displayFunctions = displayOperations(dispAudio = False, dispSpec = False, dispMelSpec = False)

    if "AUDIO" in operationString:
        displayFunctions.dispAudio = True
    if "SPEKTRUM" in operationString:
        displayFunctions.dispSpec = True
    if "MELSPEKTRUM" in operationString:
        displayFunctions.dispMelSpec = True

    return displayFunctions