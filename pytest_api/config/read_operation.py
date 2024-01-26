import yaml
import os
import sys
import json


def add_yaml_data(file, key=None, values=None,):
    """
    追加内容,保存测试中所产生的需要调用的数据到yaml
    :return:
    """
    data = {key: values}
    with open(file=file, mode='a+', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()

def rand_yaml_data(file, key=None):
    """
    读取测试中保存的数据
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # print(type(test_data), test_data)
        f.close()
        if key == None:
            return data
        return data[key]


def rand_json_apidata(file):
    """
    读取json文件中的测试api请求数据
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read()) # json转化为字段返回
        f.close()
        return data

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
    path_dir = os.path.join(os.path.join(os.getcwd(), "pytest_api", "test_underway_data", "queryProductDetail.yaml"))
    # add_yaml_data(file=path_dir, key="age", values=23)

    path_dir = os.path.join(os.path.join(os.getcwd(), "pytest_api", "test_underway_data", "queryProductDetail.yaml"))
    # print(rand_yaml_data(file=path_dir, key='user'))

    # path_dir = os.path.join(os.path.join(os.getcwd(), "pytest_api", "test_data", "queryProductDetail.json"))
    # val = rand_json_apidata(file=path_dir)
    # print(val.get("hotelId"))
    
    # clear_yaml_data(file=path_dir)
