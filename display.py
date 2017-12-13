from displayParameters import displayParameter
from Displayfunktionen import display

## Parametereingabe zur Darstellung

n_fft = 512 #Werte fuer FFT [Samples]
win_length = 10 #Fenstergroesse fuer FFT [Milli-Sekunden]
hop_length = 10 #Sprungweite fuer FFT [Milli-Sekunden]
freq_Axis = "linear" #Frequenzachse "linear" oder "log"
disp_ref = n_fft #Referenzwert fuer Spektrogramm Bildung
n_mels = 40 #Anzahl MEl-Baender
power = 2 #Exponent fuer Melspektrogram, 1 = Energie, 2 = Power
mfccs = 20 #Anzahl zu extrahierender MFCC Features

#Erzeugung des Objekts zur Parameterbuendelung
displayParameter = displayParameter(n_fft, win_length, hop_length, freq_Axis, disp_ref, n_mels, power, mfccs)

#Pfad der darzustellenden Audio-Datei
file = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios/testfile.wav'


# moegliche werte: "Audio", "Spektrum", "Melspektrum", Gross-/Kleinschreibung egal
plots = ["Audio", "Spektrum", "Melspektrum"]


display(file, displayParameter, plots)
