import Extraction_functions
import parameter

## Parameter section for extraction

n_fft = 512 #Values to use for FFT [Samples]
win_length = 40 #Windowsize for FFT [Milli-Sekunden]
hop_length = 40 #Hoplength for FFT [Milli-Sekunden]
window = "hamm" #type of window to use in stft function
symmetry = False
n_mels = 40 #number of mel bands to use
power = 2 #Exponent for Mel Spectrogram, 1 = Energy, 2 = Power
mfccs = 20 #Number of MFCC Features to extract

# moegliche werte: "MFCCS", "Spektrum", "Melspektrum", Gross-/Kleinschreibung egal
#featureArt = ["Spektrum", "Melspektrum", "MFCCS"]
feature_type = "spektrum"

#Pfade
input_path = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios'
output_path = '/home/schoeffler/PycharmProjects/DatenOrdnerTEST'

# Erzeugung des Objekts zur Parameterbuendelung
extraction_Parameter = parameter.Parameter(n_fft=n_fft, win_length=win_length, hop_length=hop_length, window=window,
                                           symmetry=symmetry, n_mels=n_mels, power=power, mfccs=mfccs)

def main():

    Extraction_functions.extract(input_path, output_path, extraction_Parameter, feature_type)

main()