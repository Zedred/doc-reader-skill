from mycroft import MycroftSkill, intent_file_handler

from os import listdir
from os.path import isfile, isdir, join

def get_files(directory):
    returnFiles = []
    if isdir(directory):
        returnFiles = [file for file in listdir(directory) if isfile(join())]
    return returnFiles

class DocReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.doc.intent')
    def handle_reader_doc(self, message):
        selection = self.get_response(dialog = 'Local or remote docs?')

        if (selection.contains('local')):
            localFiles = get_files('./readableDocuments')

            if (localFiles.__len__() > 0):
                self.speak('Select from the following which document to read:')
                selectedFile = self.ask_selection(options = localFiles)

                if (localFiles.contains(selectedFile)):
                    self.dialog('I found the files')
                else:
                    self.speak('I couldn\'t find the file')

        elif (selection.contains('remote')):
            self.speak('Remote files are not available yet. Goodbye')
            self.stop()

    def initialize(self):
        pass

    def stop(self):
        pass

def create_skill():
    return DocReader()

