'''
Created on Dec 12, 2018

@author: sylvain

see https://anthonydebarros.com/2013/02/05/get-json-from-excel-using-python-xlrd/
and
https://www.ibm.com/developerworks/library/wa-django/index.html
and
http://codetheory.in/parse-read-excel-files-xls-xlsx-javascript/

the approach 
'''
import xlrd
import numpy

class SN_QPCR_Plot(object):
    '''
    classdocs
    '''

    def __init__(self, excelFile):
        self.excelFile = excelFile
        self.data = self.readExcelSheet()
        
    def readExcelSheet(self):
        workbook = xlrd.open_workbook(self.excelFile)
        sheet = workbook.sheet_by_index(0)
        data = [[sheet.cell_value(c, r) for c in range(sheet.nrows)] for r in range(sheet.ncols)]
        return data
    
    def getGroups(self):
        itemindex = numpy.where(self.data == 7.2)
        print itemindex
        return itemindex
        

p1 = SN_QPCR_Plot('/home/sylvain/Dropbox/Perso/biostats/caro/Maddy/data.xlsx')
print(p1.excelFile)   
print p1.data[0]
print p1.data[1]
p1.getGroups()