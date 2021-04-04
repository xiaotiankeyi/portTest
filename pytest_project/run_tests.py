from pytest_project.conftest import cases_path, rerun, max_fail, REPORT_DIR
from pytest_project.public.base_module import *

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
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
        logger.info("回归模式，开始执行✈✈！")
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
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
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
    # run(m='run')
    # os.system("rd report_result /s/q")
    # os.system("rd report /s/q")
    # Runner()
    # pytest.main(['-vs', 'pytest_project::testcases::test_Userlogin.py::Testlogin::test_case_01', '--alluredir report'])
    # os.system('allure generate --clean report/ -o report_result/html')
    pass