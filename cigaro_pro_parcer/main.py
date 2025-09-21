import xlsxwriter
from parcer_abc import array_abc
from parcer_wine import array_wine

book = xlsxwriter.Workbook(r"C:\Users\SOLOMON\Desktop\data.xlsx")
page_abc = book.add_worksheet('Абсент')
page_wine = book.add_worksheet('Вино')

row_abc = 0
col_abc = 0

page_abc.set_column("A:A", 60)
page_abc.set_column("B:B", 60)
page_abc.set_column("C:C", 10)


for item in array_abc():
    page_abc.write(row_abc, col_abc, item[0])
    page_abc.write(row_abc, col_abc+1, item[1])
    page_abc.write(row_abc, col_abc+2, item[2])
    row_abc += 1

row_wine = 0
col_wine = 0

page_wine.set_column("A:A", 60)
page_wine.set_column("B:B", 60)
page_wine.set_column("C:C", 10)

for item in array_wine():
    page_wine.write(row_wine, col_wine, item[0])
    page_wine.write(row_wine, col_wine + 1, item[1])
    page_wine.write(row_wine, col_wine+2, item[2])
    row_wine += 1

book.close()
