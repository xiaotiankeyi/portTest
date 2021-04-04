
from pytest_project.public.base_module import *


class HandleExcel():
    """封装操作excel的方法"""

    def __init__(self, file=Excel_path, sheet_id=None, sheet_name=None):
        self.file = file
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        self.data = self.get_Excel()

    # 打开文件,获取某一页sheet对象
    def get_Excel(self):
        data = xlrd.open_workbook(self.file)
        # sheet = data.sheet_by_index(self.sheet_id)
        sheet = data.sheet_by_name(self.sheet_name)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # # 向某个单元格写入数据
    # def write_values(self, row, col, value):
    #     data = xlrd.open_workbook(self.file)
    #     data_copy = copy(data)
    #     sheet = data_copy.get_sheet(0)
    #     sheet.write(row, col, value)
    #     data_copy.save(self.file_dir)

    # 封装excel的列名常量
    def get_caseseq(self):
        """获取用例序号"""
        caseSeq = 0
        return caseSeq

    def get_testpoint(self):
        """获取测试功能"""
        testpoint = 2
        return testpoint

    def get_YN(self):
        """获取是否执行"""
        yn = 3
        return yn

    def get_host(self):
        """获取请求域名"""
        host = 4
        return host

    def get_urlxpath(self):
        """获取请求路径"""
        urlxpath = 5
        return urlxpath

    def get_method(self):
        """获取method请求方式"""
        method = 6
        return method

    def get_headers(self):
        """获取请求头"""
        headers = 7
        return headers

    def get_data(self):
        """获取params请求参数"""
        params = 8
        return params

    def get_assert(self):
        """获取断言内容"""
        expect = 9
        return expect


if __name__ == '__main__':
    test = HandleExcel(sheet_name='接口测试')
    # print(test.get_Excel().name)
    # print(test.get_rows())
    # print(test.get_value(0,8))
    d = test.get_value(1,8)
    print(type(d), d)
    d = eval(d)
    print(type(d), d)
