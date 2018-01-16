import matplotlib.pyplot as mp
import InOut
import FeatureVisualisation

#Dictionary providing appropriate function for specific operation
displayDictionary = {
    "AUDIO": FeatureVisualisation.displayAudio,
    "SPEKTRUM": FeatureVisualisation.displaySpectrogram,
    "MELSPEKTRUM": FeatureVisualisation.displayMelSpectrogram
}

#Darstellungsfunktion
def display(filepath, displayParameter, stringList):

    displayParameter.setOperations(stringList)
    displayParameter.checkIntegrity()
    y, sr, file = InOut.readInAudioDirectly(filepath)
    [displayDictionary[displayOperation](y, sr, file, displayParameter) for displayOperation in displayParameter.operations]
    mp.show()
    return None
