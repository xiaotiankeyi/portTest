import yaml
import os
import xlrd

base_path = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_path + '/test_data/login_test.yaml')
Excel_path = os.path.join(base_path + '/test_data/Testdata.xlsx')

def rand_excel():
    """读取excel文件"""
    data = xlrd.open_workbook(Excel_path)
    sheet = data.sheet_by_index(1)

    nrows = sheet.nrows
    ncols = sheet.ncols

    case = []
    for i in range(1, sheet.nrows):
        if sheet.row_values(i)[3] == 'Y':
            case.append(sheet.row_values(i))
    return case

def add_yaml_data(file, key=None, values=None,):
    """
    追加内容
    :return:
    """
    data = {key: values}
    with open(file=file, mode='a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()

def rand_yaml_data(file, key=None):
    """
    读取
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        return data

def clear_yaml_data(file,):
    """
    清除测试数据
    :return:
    """
    with open(file=file, mode='w', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()
        f.close()

if __name__ == "__main__":
    # add_yaml_data()
    # print(rand_yaml_data(file=data_path, key=None))
    # clear_yaml_data(file='config_data.yaml')
    rand_excel()
    pass
