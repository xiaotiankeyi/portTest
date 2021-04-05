from pytest_project.public.base_module import *
import yaml
import xlrd
import os

base_path = os.path.dirname(os.path.dirname(__file__))
Excel_path = os.path.join(base_path + '/test_data/Testdata.xlsx')

def rand_excel(sheet_name):
    """读取excel文件,实现@pytest.mark.parametrize参数化运行"""
    data = xlrd.open_workbook(Excel_path)
    # sheet = data.sheet_by_index(1)
    sheet = data.sheet_by_name(sheet_name=sheet_name)

    nrows = sheet.nrows
    ncols = sheet.ncols

    case = []
    for i in range(1, sheet.nrows):
        if sheet.row_values(i)[3] == 'Y':
            case.append(sheet.row_values(i))
    return case

def add_yaml_data(file, key=None, values=None,):
    """
    追加内容,保存测试中所产生的需要调用的数据
    :return:
    """
    data = {key: values}
    with open(file=file, mode='a+', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()

def rand_yaml_apidata(file):
    """
    读取yaml文件中的测试用例数据
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        return data

def rand_yaml_testdata(file, key=None):
    """
    读取yaml文件中的测试用例数据和测试过中保存的数据
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        return data[key]

def clear_yaml_data(file,):
    """
    清除测试过程中保存的数据
    :return:
    """
    with open(file=file, mode='w', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()        #清空文件内容
        f.close()

if __name__ == "__main__":
    # val = rand_excel(sheet_name='接口测试')
    # print(val)
    # add_yaml_data(file=test_data_path, key='token', values='sdsdhaskldahd1378737127381')
    # val = rand_yaml_apidata(file=api_data_path)
    # print(val)
    val = rand_yaml_testdata(file=testapi_data_path+'register_test.yaml', key='teststeps3')
    print(val)
    # clear_yaml_data(file=test_data_path)
    pass
