import Extractionfunctions
import parameter

## Parameter section for extraction

n_fft = 2048#512 #Values to use for FFT [Samples]
win_length = 40 #Windowsize for FFT [Milli-Sekunden]
hop_length = 40 #Hoplength for FFT [Milli-Sekunden]
window = "hann" #type of window to use in stft function
symmetry = True#False
n_mels = 128 #40 #number of mel bands to use
power = 2 #Exponent for Mel Spectrogram, 1 = Energy, 2 = Power
mfccs = 20 #Number of MFCC Features to extract

# moegliche werte: "MFCCS", "Spektrum", "Melspektrum", Gross-/Kleinschreibung egal
#featureArt = ["Spektrum", "Melspektrum", "MFCCS"]
featureArt = "spektrum"

#Pfade
inputpath = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios'
outputpath = '/home/schoeffler/PycharmProjects/DatenOrdnerTEST'

# Erzeugung des Objekts zur Parameterbuendelung
extraktionsParameter = parameter.Parameter(n_fft=n_fft, win_length=win_length, hop_length=hop_length, n_mels=n_mels, power=power, mfccs=mfccs)

def main():

    Extractionfunctions.extract(inputpath, outputpath, extraktionsParameter, featureArt)

main()