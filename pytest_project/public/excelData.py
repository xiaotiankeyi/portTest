from pytest_project.public.readExcel import HandleExcel
from pytest_project.public.base_module import *

# base_url = "http://127.0.0.1:7777"

def accept(row, sheet_name=None):
    """封装excel数据读取的代码"""

    obj = HandleExcel(sheet_name=sheet_name)

    yn = obj.get_value(row, obj.get_YN())
    url = obj.get_value(row, obj.get_urlxpath())
    method = obj.get_value(row, obj.get_method())
    headers = eval(obj.get_value(row, obj.get_headers()))
    data = eval(obj.get_value(row, obj.get_data()))
    data = json.dumps(data)
    assert_val = obj.get_value(row, obj.get_assert())

    return (yn, url, method, headers, data, assert_val)
if __name__ == "__main__":
    # a = accept(row=1, sheet_name='登录')
    # print(a)
    # print(a[3], type(a[3]))
    # print(a[4], type(a[4]))
    pass