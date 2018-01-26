def calc_Samples(time, sr):
    win_Leng = int(time * 0.001 * sr) # Factor 0.001, as time in milliseconds [ms]
    return win_Leng

#Function to ensure n_fft >= win_length
def check_FFT_Samples(n_fft, win_length):
    if win_length > n_fft:
        n_fft_out = win_length
    else:
        n_fft_out = n_fft
    return n_fft_out

