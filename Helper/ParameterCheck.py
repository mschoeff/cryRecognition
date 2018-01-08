from getOperations import capitalizeStrings, getExtractionOperations, getDisplayOperations

#Funktion um Sampleanzahl aus gegebener Zeitdauer und Samplingrate zu berechnen
def calcSamples(time, sr):
    winLeng = int(time * 0.001 * sr) # Faktor 0.001, da Zeit [ms]
    return winLeng

#Funktion um n_fft >= win_length zu gewaehrleisten
def checkFFTSamples(n_fft, win_length, sr):
    if calcSamples(win_length, sr) > n_fft:
        n_fft_out = calcSamples(win_length, sr)
    else:
        n_fft_out = n_fft
    return n_fft_out

#Funktion generiert auszufuehrende Extraktions-Operationen und ueberprueft Parameter
def checkExtractionParameterIntegrity(stringList, parameter):
    operationString = capitalizeStrings(stringList)
    extractionFunctions = getExtractionOperations(operationString)
    parameter.n_fft = checkFFTSamples(parameter.n_fft, parameter.win_length, 22050) #sr ist set to 22050 as default
    parameter.hop_length = calcSamples(parameter.hop_length, 22050)
    parameter.win_length = calcSamples(parameter.win_length, 22050)

    #return (extractionFunctions, parameter)
    return extractionFunctions

#Funktion generiert auszufuehrende Darstellungs-Operationen und ueberprueft Parameter
def checkDisplayParameterIntegrity(stringList, parameter):
    operationString = capitalizeStrings(stringList)
    displayFunctions = getDisplayOperations(operationString)
    parameter.n_fft = checkFFTSamples(parameter.n_fft, parameter.win_length, 22050) #sr ist set to 22050 as default
    parameter.hop_length = calcSamples(parameter.hop_length, 22050)
    parameter.win_length = calcSamples(parameter.win_length, 22050)

    #return (displayFunctions, parameter)
    return displayFunctions
