from mycroft import MycroftSkill, intent_file_handler


class DocReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.doc.intent')
    def handle_reader_doc(self, message):
        self.speak_dialog('reader.doc')


def create_skill():
    return DocReader()

