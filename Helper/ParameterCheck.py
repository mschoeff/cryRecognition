
#Funktion um Sampleanzahl aus gegebener Zeitdauer und Samplingrate zu berechnen
def calcSamples(time, sr):
    winLeng = int(time * 0.001 * sr) # Faktor 0.001, da Zeit [ms]
    return winLeng

#Funktion um n_fft >= win_length zu gewaehrleisten
def checkFFTSamples(n_fft, win_length):
    if win_length > n_fft:
        n_fft_out = win_length
    else:
        n_fft_out = n_fft
    return n_fft_out

