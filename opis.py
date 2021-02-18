import openpyxl
open_file_excel = openpyxl.reader.excel.load_workbook(filename = 'Копия Опись документации ОКР.xlsx')

open_file_excel.active = 0
sheet = open_file_excel.active
#for i in range(1,211):
#    print(sheet['A'+ str(i)].value, sheet['B'+str(i)].value, sheet['C' +str(i)].value)

import pandas as pd
open_file_excel = pd.read_excel('Копия Опись документации ОКР.xlsx', sheet_name = 'Лист1', engine = 'openpyxl')
print(open_file_excel)
