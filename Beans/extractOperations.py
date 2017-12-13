#Class for choosing extracting operations to be conducted
class extractOperations(object):
    def __init__(self, saveSpec = True, saveMelSpec = True, saveMFCCs = True):
        self.saveSpec = saveSpec
        self.saveMelSpec = saveMelSpec
        self.saveMFCCs = saveMFCCs

