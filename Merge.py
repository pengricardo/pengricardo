# -*- coding: utf-8 -*-
# 将所有excel文件中相同单元格为的数据相加
# 1.读取所有excel文件，并实现输入文件名就能读取该excel文件
import xlrd
import xlwt
import xlsxwriter
import os
input1 = input('请输入第一个excel文件名：')
input2 = input('请输入第二个excel文件名：')
input3 = input('请输入第三个excel文件名：')
read1 = xlrd.open_workbook(input1)
read2 = xlrd.open_workbook(input2)
read3 = xlrd.open_workbook(input3)
# 2.遍历所有的表格
for sheet in read1.sheets():
    # 3.遍历所有的行
    for row in range(sheet.nrows):
        # 4.遍历所有的列
        for col in range(sheet.ncols):
            # 5.查看每个不为数值的单元格是否相等，如果相等则打印出来，如果不相等则报错说表格格式不一致
            if sheet.cell(row,col).value != sheet.cell(row,col).value:
                print('表格格式不一致')
            else:
                print(sheet.cell(row,col).value)
# 6.将相同行列单元格的数据相加
print(sheet.cell(row,col).value + sheet.cell(row,col).value)
# 7.将相加后的数据和上面打印出来的相等的不为数值的单元格写入新的excel文件中
merge = xlsxwriter.Workbook('new.xlsx')
worksheet = merge.add_worksheet()
worksheet.write(row,col,sheet.cell(row,col).value + sheet.cell(row,col).value)
# 8.将新的excel文件保存到桌面
merge.close()



