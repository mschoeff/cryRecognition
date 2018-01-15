import Displayfunktionen
import parameter

## Parametereingabe zur Darstellung

n_fft = 1024 #Werte fuer FFT [Samples]
win_length = 10 #Fenstergroesse fuer FFT [Milli-Sekunden]
hop_length = 10 #Sprungweite fuer FFT [Milli-Sekunden]
window = "hann"
symmetry = False
freq_Axis = "linear" #Frequenzachse "linear" oder "log"
disp_ref = n_fft #Referenzwert fuer Spektrogramm Bildung
n_mels = 40 #Anzahl MEl-Baender
power = 2 #Exponent fuer Melspektrogram, 1 = Energie, 2 = Power
mfccs = 20 #Anzahl zu extrahierender MFCC Features

#Erzeugung des Objekts zur Parameterbuendelung
displayParameter = parameter.Parameter(n_fft, win_length, hop_length, window, symmetry, n_mels, power, mfccs, freq_Axis, disp_ref)

#Pfad der darzustellenden Audio-Datei
file = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios/testfile.wav'


# moegliche werte: "Audio", "Spektrum", "Melspektrum", Gross-/Kleinschreibung egal
plots = ["spektrum", "audio", "melspektrum"]


def main():

    Displayfunktionen.display(file, displayParameter, plots)

main()
