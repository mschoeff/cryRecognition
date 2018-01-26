import Folder_Operations
import In_Out
import Spectral_Features
import normalizer

#Dictionary providing appropriate function for specific operation
operationDictionary = {
    "SPEKTRUM": Spectral_Features.compute_Power_Spectrogram,
    "MELSPEKTRUM": Spectral_Features.compute_Mel_Spectrum,
    "MFCCS": Spectral_Features.compute_MFCC
}

#Function that calls appropriate extraction function based on operation to be performed
def extraction_of_Features(parameter, y):

    feature = operationDictionary[parameter.operations](y, parameter)
    return feature

#Extractionfunction
def extract(input_Folder, output_Folder, parameter, string_List):

    parameter.set_Operations(string_List)
    parameter.check_Integrity()
    audio_list = In_Out.list_Audios(input_Folder)
    Folder_Operations.create_output_folders(output_Folder, parameter)

    Normalizer = normalizer.Normalizer(parameter)

    for file in audio_list:

        y, sr, filename = In_Out.read_In_Audio(input_Folder, file)
        feature = extraction_of_Features(parameter, y)
        Folder_Operations.save_Features(feature, parameter, output_Folder, filename)
        Normalizer.add_Feature(feature)

    Normalizer.calc_Arith_Means() #Standard Deviation not yet implemented
    Normalizer.save_Arith_Means(parameter, output_Folder)

    return None




