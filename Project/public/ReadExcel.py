import xlrd
import os
from xlutils.copy import copy

'''
用于封装对Excel表的操作
'''


class HandleExcel():
    """封装操作excel的方法"""
    file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data\\Testdata.xlsx')

    def __init__(self, file=file_dir, sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()

    # 打开文件,获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_values(self, row, col, value):
        data = xlrd.open_workbook(self.file)
        data_copy = copy(data)
        sheet = data_copy.get_sheet(0)
        sheet.write(row, col, value)
        data_copy.save(self.file_dir)

    # 封装excel的列名常量
    def get_caseseq(self):
        """获取caseSeq用例序号"""
        caseSeq = 0
        return caseSeq

    def get_apiName(self):
        """获取apiName用例名称"""
        apiName = 2
        return apiName

    def get_host(self):
        """获取Host"""
        url = 3
        return url

    def get_urlxpath(self):
        """获取method请求方式"""
        urlxpath = 4
        return urlxpath

    def get_method(self):
        """获取method请求方式"""
        method = 5
        return method

    def get_params(self):
        """获取params请求参数"""
        params = 7
        return params

    def get_verifyID(self):
        """获取expectValue断言ID"""
        expect = 8
        return expect

    def get_resultvalue(self):
        """获取要写入数据的单元格"""
        expect = 9
        return expect


if __name__ == '__main__':
    test = HandleExcel()
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(1, 7))
