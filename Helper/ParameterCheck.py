def calcSamples(time, sr):
    winLeng = int(time * 0.001 * sr) # Factor 0.001, as time in milliseconds [ms]
    return winLeng

#Function to ensure n_fft >= win_length
def checkFFTSamples(n_fft, win_length):
    if win_length > n_fft:
        n_fft_out = win_length
    else:
        n_fft_out = n_fft
    return n_fft_out

