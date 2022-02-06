import numpy as np
import xlrd
import csv

#doc = xlrd.open_workbook('../Data/iris.xls').sheet_by_index(0)
doc = xlrd.open_workbook('../Data/thomas/train_and_test2.csv').sheet_by_index(0)
with open('../Data/thomas/train_and_test2.csv',mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)