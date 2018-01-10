import Extraktionsfunktionen
import parameter

## Parametereingabe zur Merkmalsextraktion

n_fft = 512 #Werte fuer FFT [Samples]
win_length = 40 #Fenstergroesse fuer FFT [Milli-Sekunden]
hop_length = 40 #Sprungweite fuer FFT [Milli-Sekunden]
n_mels = 40 #Anzahl MEl-Baender
power = 2 #Exponent fuer Melspektrogram, 1 = Energie, 2 = Power
mfccs = 20 #Anzahl zu extrahierender MFCC Features

# moegliche werte: "MFCCS", "Spektrum", "Melspektrum", Gross-/Kleinschreibung egal
#featureArt = ["Spektrum", "Melspektrum", "MFCCS"]
featureArt = "mfccs"

#Pfade
inputpath = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios'
outputpath = '/home/schoeffler/PycharmProjects/DatenOrdnerTEST'

# Erzeugung des Objekts zur Parameterbuendelung
extraktionsParameter = parameter.Parameter(n_fft, win_length, hop_length, n_mels, power, mfccs)

def main():

    Extraktionsfunktionen.extract(inputpath, outputpath, extraktionsParameter, featureArt)

main()