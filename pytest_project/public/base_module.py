from pytest_project.public import test_period
from pytest_project.log.log import handle
from pytest_project.public.requestway import RunMain
from pytest_project.config.read_yaml import rand_yaml_data, add_yaml_data, rand_excel
import os
import json
import pytest
import xlrd
import time
import allure
import sys

#基础目录
base_path = os.path.dirname(os.path.dirname(__file__))
# print('待添加添加',base_path)
# sys.path.append(base_path)
# print(os.environ)
#测试api用例目录
api_data_path = os.path.join(base_path + '/test_data/login_test.yaml')
#日志文件目录
log_path = os.path.join(base_path + '/log/outputLog.log')
#Excel数据目录
Excel_path = os.path.join(base_path + '/test_data/Testdata.xlsx')
#测试数据保存目录
test_data_path = os.path.join(base_path + '/test_data/test_data.yaml')
log = handle(file=log_path)
startup = test_period.startup

request = RunMain()


if __name__ == "__main__":
    pass