import os
import librosa

def list_Files(folder):
    return os.listdir(folder)

def list_Audios(folder):
    first_list = os.listdir(folder)
    audio_list = []
    for file in first_list:
        if file.endswith('.mp3') or file.endswith('.wav'):
            audio_list.append(file)
    return audio_list

def read_In_Audio(folder, file):
    file_name, file_extension = os.path.splitext(file)
    y, sr = librosa.load(folder + '/' + file, mono = True)
    return (y, sr, file_name)

def read_In_Audio_Directly(filepath):
    y, sr = librosa.load(filepath)
    file_name, file_extension = os.path.splitext(filepath)
    return (y, sr, file_name)

