import os
import sys

sys.path.append(os.path.join(os.getcwd(), "pytest_api"))

import pytest
from public.base_module import *
from conftest import cases_path, rerun, max_fail, REPORT_DIR

'''
说明:
1、用例创建原则,测试文件名必须以“test”开头,测试函数必须以“test”开头。
2、运行方式:
  > python3 run_tests.py  (回归模式,生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
'''

def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")

def run(m):
    if m is None or m == "run":
        logger.info("回归模式,开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        html_report = os.path.join(REPORT_DIR, now_time, "report.html")
        xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
        pytest.main(["-s", "-v", cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", max_fail,
                     "--reruns", rerun])
        logger.info("运行结束,生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式,开始执行！")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


def Runner():
    pytest.main([
        "-s", "-v", "-q", cases_path,
        "--alluredir", 'report',
        "--maxfail", max_fail,
        "--reruns", rerun,
    ])

#终端执行命令
#pytest -s -v testcases --maxfail 5 --reruns 2 --alluredir report
#allure generate --clean report/ -o report_result/html
if __name__ == '__main__':
    sys.path.append(os.path.join(os.getcwd(), "pytest_api"))

    # run(m='run')
    # os.system("rd report_result /s/q")
    # os.system("rd report /s/q")
    # Runner()
    # pytest.main([cases_path,'-vs', "--html", "report/html/report.html"])
    # pytest.main([cases_path,'-vs', "--alluredir", "report/allure/"])
    # os.system('allure generate ./report/allure -o ./report/allure_redult/')
    # os.system('allure open ./report/allure_redult/')
    # os.system('allure serve ./report/allure/')


    pass