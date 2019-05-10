import time
from win32com.client import Dispatch


class Word(object):
    def __init__(self, path, visible=False):
        self.word = Dispatch("Word.Application")
        self.word.Visible = visible
        self.doc = word.Documents.Open(path)

    def replace(self, old_str, new_str):
        self.word.Selection.Find.Execute(old_str, False, False, False, False, False, True, 1, True, new_str, 2)

    def save(self):
        self.doc.Save()
        self.doc.Close()
