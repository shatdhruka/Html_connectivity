import xlrd

loc=("C:/Users/Administrator/Desktop/Sample.xls")

wb = xlrd. open_workbook(loc)
sheet = wb . sheet_by_index(0)

sheet.cell_value(0, 0)
print(sheet . nrows)
