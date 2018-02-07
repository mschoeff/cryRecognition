import matplotlib.pyplot as mp
import numpy as np
import In_Out
import Extraction_functions
import librosa.display as libdisp

#Displayfunction
def display(filepath, parameter, stringList):

    parameter.set_Operations(stringList)
    parameter.check_Integrity()
    y, sr, file = In_Out.read_In_Audio_Directly(filepath)

    visualize_features(y, sr, file, parameter)

    mp.show()
    return None

def visualize_features(y, sr, file, parameter):
    number_of_plots = len(parameter.operations)
    for operation in parameter.operations:
        mp.subplot(number_of_plots, 1, parameter.operations.index(operation)+1)
        if 'AUDIO' in operation:
            displayAudio(y, sr, file)
        else:
            feature = Extraction_functions.operation_Dictionary[operation](y, parameter)
            display_single_feature(feature, parameter, operation)
    return None

def display_single_feature(y, parameter, operation):
    libdisp.specshow(y, cmap = 'gray_r', y_axis = parameter.display_Dictionary[operation])
    mp.colorbar(orientation='horizontal')
    mp.title(parameter.display_Dictionary[operation] + '-scaled frequency axis ' + operation)
    return None

def displayAudio(y, sr, filename):
    mp.title(filename)
    time = np.linspace(0, len(y)/sr, len(y))
    mp.plot(time, y)
    return None