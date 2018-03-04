#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import sys
import io
def export_data(filename):
    # open a excel file
    workbook = xlrd.open_workbook(filename)
    file = open('output.txt', 'w', encoding='utf-8')
    sheets = workbook.sheets()
    last = ['','','','','','','','','']
    k = 1
    for x in range(len(sheets)):
        sheet = sheets[x]
        for i in range(2, sheet.nrows):
            row_data = sheet.row(i)
            line = ''
            for j in range(len(row_data)):
                if row_data[j].value == '':
                    row_data[j] = last[j]
                else:
                    last[j] = row_data[j]
                    if j == 0:
                        k = k + 1
                if row_data[j].ctype == xlrd.XL_CELL_TEXT:
                    line = line + row_data[j].value + '|'
                elif j == 1:
                    line = line + str(int(row_data[j].value)+ k * 100000) + '|'
                elif j == 8:
                    line = line + str(int(row_data[j].value))
                else:
                    line = line + str(row_data[j].value) + '|'
            file.writelines(line + '\n')
    file.close()


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    export_data('/Users/jagenzhao/Documents/词包选择.xlsx')
