import os
import sys

sys.path.append(os.path.join(os.getcwd(), "pytest_api"))

from public.test_period import startup
from public.requestway import RunMain
from config.read_operation import rand_json_apidata
from config.read_operation import add_yaml_data
from config.read_operation import rand_yaml_data
from config.read_operation import clear_yaml_data
from logs.log import handle
import json
import pytest
import time
import allure
import yaml


#基础目录
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

#测试api用例目录,没有写死文件
testapi_data_path = os.path.join(base_path, 'test_data')

#日志信息写入文件目录
log_path = os.path.join(base_path, 'logs', 'outputLog.log')

#测试数据保存目录
test_data_path = os.path.join(base_path, 'test_underway_data')

# 测试结果保存路径
test_result_report = os.path.join(base_path, "report")

#调用日志
logger = handle(file=log_path)

#调用fixture
startup = startup

#调用请求方式
request = RunMain()


if __name__ == "__main__":
    pass