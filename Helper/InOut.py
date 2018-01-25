import os
import librosa

def listFiles(folder):
    return os.listdir(folder)

def listAudios(folder):
    firstList = os.listdir(folder)
    audioList = []
    for file in firstList:
        if file.endswith('.mp3') or file.endswith('.wav'):
            audioList.append(file)
    return audioList

def readInAudio(folder, file):
    filename, file_extension = os.path.splitext(file)
    y, sr = librosa.load(folder + '/' + file, mono = True)
    return (y, sr, filename)

def readInAudioDirectly(filepath):
    y, sr = librosa.load(filepath)
    filename, file_extension = os.path.splitext(filepath)
    return (y, sr, filename)

