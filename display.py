import Displayfunctions
import parameter

## Parameter section for displaying

n_fft = 1024 #Values to use for FFT [Samples]
win_length = 10 #Windowsize for FFT [Milli-Sekunden]
hop_length = 10 #Hoplength for FFT [Milli-Sekunden]
window = "hann" #type of window to use in stft function
symmetry = False
frequency_Axis = "linear" #frequency axis "linear" or "log"
disp_ref = n_fft #reference value for spectrogramm
n_mels = 40 #number of mel bands to use
power = 2 #Exponent for Mel Spectrogram, 1 = Energy, 2 = Power
mfccs = 20 #Number of MFCC Features to extract

#Parameters are fused in an object
displayParameter = parameter.Parameter(n_fft=n_fft, win_length=win_length, hop_length=hop_length, window=window,
                                       symmetry=symmetry, n_mels=n_mels, power=power,
                                       mfccs=mfccs, frequency_Axis=frequency_Axis, disp_Ref=disp_ref)


#Path to the audio file to be displayed
file = '/home/schoeffler/PycharmProjects/spectrogram_1/Audios/testfile.wav'


# possible values: "Audio", "Spektrum", "Melspektrum", capitalization is not important
plots = ["audio", "db_spektrum", "spektrum"]


def main():

    Displayfunctions.display(file, displayParameter, plots)

main()
