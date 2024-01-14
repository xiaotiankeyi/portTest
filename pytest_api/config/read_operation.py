import yaml
import os
import sys


def add_yaml_data(file, key=None, values=None,):
    """
    追加内容,保存测试中所产生的需要调用的数据
    :return:
    """
    data = {key: values}
    with open(file=file, mode='a+', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()

def rand_yaml_data(file, key=None):
    """
    读取
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        if key == None:
            return data
        return data[key]


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
    读取yaml文件中的测试用例数据和测试过程中保存的数据
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        return data[key]

def clear_yaml_data(file):
    """
    清除测试过程中保存的数据
    :return:
    """
    with open(file=file, mode='w', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()        #清空文件内容
        f.close()

if __name__ == "__main__":
    # add_yaml_data()
    # print(os.getcwd())
    print(os.path.dirname(os.path.abspath(__file__)))
    config_path_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_data.yaml")
    # print(path_dir)
    print(rand_yaml_data(file=config_path_dir, key='db'))

    # print(rand_yaml_data(file="config_data.yaml", key='db'))
    pass
