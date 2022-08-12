import sys
from wordhoard import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
# synonym = Synonyms(search_string='mother')
# synonym_results = synonym.find_synonyms()
# print(synonym_results)
# ['ancestor', 'biological mother', 'birth mother', 'child-bearer', 'creator',
#  'dam', 'female parent', 'forebearer', 'foster mother', 'ma', 'mama', 'mamma',
#  'mammy', 'mater', 'mom', 'momma', 'mommy', 'mother-in-law', 'mum', 'mummy',
#  'old lady', 'old woman', 'origin', 'para i', 'parent', 'predecessor',
#  'primipara', 'procreator', 'progenitor', 'puerpera', 'quadripara',
#  'quintipara', 'source', 'supermom', 'surrogate mother']


class UI_dict(QWidget):
    def __init__(self):
        super(UI_dict, self).__init__()
        uic.loadUi("interface.ui", self)
        self.pushButton.clicked.connect(lambda: self.apply())

    def apply(self):
        word = self.lineEdit.text()
        definition = Definitions(search_string=word)
        definition_results = definition.find_definitions()
        label = ''.join(definition_results)
        self.label.setText(str(label))

        synonym = Synonyms(search_string=word)
        synonym_results = synonym.find_synonyms()
        label2 = ''.join("/ " + x + " /" for x in synonym_results)
        self.label_2.setText(str(label2))

        antonym = Antonyms(search_string=word)
        antonym_results = antonym.find_antonyms()
        label3 = ''.join("/ " + x + " /" for x in antonym_results)
        self.label_3.setText(str(label3))


app = QApplication(sys.argv)
window = UI_dict()
window.show()
app.exec_()
