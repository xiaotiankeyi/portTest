from base_module import *

def accept(file, file_name, key):
    """获取yaml文件单个测试用例,和获取测试过程中产生的数据"""
    data = rand_yaml_testdata(file=file + file_name, key=key)
    return data

if __name__ == "__main__":
    # val = accept(file=testapi_data_path,file_name='register_test.yaml', key='teststeps3')
    # print(val)
    pass