import os
import librosa


#Funktion zur Auflistung der Dateien im Verzeichnis
def listFiles(folder):
    '''returns list with filenames in folder'''
    return os.listdir(folder)

#Funktion zur Extraktion der Audiodateien in einer Liste
def listAudios(firstlist):
    '''returns a new list containing only the audio files of firstlist'''
    audioList = []
    for file in firstlist:
        if file.endswith('.mp3') or file.endswith('.wav'):
            audioList.append(file)
    return audioList

#Funktion zum Einlesen einer Audiodatei aus Ordner
def readInAudio(folder, file):
    filename, file_extension = os.path.splitext(file)
    y, sr = librosa.load(folder + '/' + file)
    return (y, sr, filename)

#Funktion zum Einlesen einer Audiodatei aus Dateipfad
def readInAudioDirectly(filepath):
    y, sr = librosa.load(filepath)
    filename, file_extension = os.path.splitext(filepath)
    return (y, sr, filename)
