import time
import xlrd
from xlutils.copy import copy


class Excel(object):
    def __init__(self, path):
        self.path = path
        self.rb = xlrd.open_workbook(path)
        self.rs = self.rb.sheets()[0]
        self.wb = copy(self.rb)
        self.ws = self.wb.get_sheet(0)

    def sheet(self, sheet):
        if type(sheet) == str:
            self.rs = self.rb.sheet_by_name(sheet)
            self.ws = self.wb.get_sheet(sheet)
        elif type(sheet) == int:
            self.rs = self.rb.sheet_by_index(sheet)
            self.ws = self.wb.get_sheet(sheet)

    def get(self, row, col):
        return self.rs.cell_value(rowx=row, colx=col)

    def write(self, row, col, text):
        self.ws.write(row, col, text)

    def save(self):
        self.wb.save(self.path)
