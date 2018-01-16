def stftSize(parameter):
    return 1 + parameter.n_fft / 2


def melSize(parameter):
    return parameter.n_mels


def mfccSize(parameter):
    return parameter.mfccs