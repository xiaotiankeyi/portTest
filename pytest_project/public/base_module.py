from pytest_project.public import test_period
from pytest_project.log.log import handle
from pytest_project.public.requestway import RunMain
from pytest_project.config.read_operation import rand_yaml_apidata
from pytest_project.config.read_operation import add_yaml_data
from pytest_project.config.read_operation import rand_excel
from pytest_project.config.read_operation import rand_yaml_testdata
from pytest_project.config.read_operation import clear_yaml_data
import os
import json
import pytest
import time
import allure
import sys
import xlrd
import yaml

#基础目录
base_path = os.path.dirname(os.path.dirname(__file__))
# print('待添加添加',base_path)
# sys.path.append(base_path)
# print(os.environ)
#测试api用例目录
api_data_path = os.path.join(base_path + '/test_data/login_test.yaml')
#测试api用例目录没有写死文件
testapi_data_path = os.path.join(base_path + '/test_data/')
#日志信息写入文件目录
log_path = os.path.join(base_path + '/log/outputLog.log')
#Excel数据目录
Excel_path = os.path.join(base_path + '/test_data/Testdata.xlsx')
#测试数据保存目录
test_data_path = os.path.join(base_path + '/test_data/test_data.yaml')
#调用日志
logger = handle(file=log_path)
#调用fixture
startup = test_period.startup
#调用请求方式
request = RunMain()


if __name__ == "__main__":
    pass