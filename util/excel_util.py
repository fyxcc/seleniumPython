# coding=utf-8
import xlrd
import os
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = os.path.join(os.path.pardir + "/data/" + "keyword.xls")
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        # 打开 excel 文件，获取数据列表
        self.data = xlrd.open_workbook(self.excel_path)
        # 读取第一 sheet 页的数据
        self.table = self.data.sheets()[index]

    # 获取excel数据，每一行保存为一个list,最后存储在一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                # 获取第i行每一列的数据
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据(行号与列号）
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    excel_path = os.path.join(os.path.pardir + "/data/ " + "keyword.xls")
    ex = ExcelUtil(r"D:\pythonWork\untitled2\data\keyword.xls")
    # print(ex.get_col_value(0,4))
    print(ex.write_value(3, 'test'))
