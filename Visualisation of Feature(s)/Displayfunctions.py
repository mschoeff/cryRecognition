import matplotlib.pyplot as mp
import InOut
import FeatureVisualisation
import SpectralFeatures

#Dictionary providing appropriate function for specific operation
displayDictionary = {
    "AUDIO": FeatureVisualisation.displayAudio,
    "SPEKTRUM": FeatureVisualisation.displaySpectrogram,
    "MELSPEKTRUM": FeatureVisualisation.displayMelSpectrogram,
    "DB_SPEKTRUM": FeatureVisualisation.displayDBSpectrogram
}

#Displayfunction
def display(filepath, displayParameter, stringList):

    displayParameter.setOperations(stringList)
    displayParameter.checkIntegrity()
    y, sr, file = InOut.readInAudioDirectly(filepath)

    ##displayStuff

    [displayDictionary[displayOperation](y, sr, file, displayParameter) for displayOperation in displayParameter.operations]
    mp.show()
    return None

#def displaystuff(y, sr, file, displayParameter):

 #   for operation in displayParameter.operationDictionary:

        #nackte featurewerte berecvhnen, genauso wie dus bei der featureextarction machst!
    #    feature = welcheFunktionAuchImmerdieFeaturesBerechnet[operation]

        #berechnen, wo der subplot hinwandern muss. Ergibt sich funktional aus pos in liste und | operations |
    #    subplot(berechneWohin)

        ## display tatsaechlich aufrufen. In dieser Funktion drin werden, in abhaengigkeit zu der uebergebenen operation, die die
        ## displayparameter berechnet. beispiel: Immer, wenn "db_spektrum" kommt, schreib "DB-spektrum" drueber und eine db-skale drunter.
        ## vielleicht erfindest du dafuer eine extra dictionary.

   #     RufeLibrosaDisplayFunktionAuf(feature, operation)