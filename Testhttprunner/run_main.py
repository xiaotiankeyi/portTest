import os
import time
import unittest
from BSTestRunner import BSTestRunner

# 运行测试的路径
run_xpath = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)),
    'testcases')
# print(run_xpath)

# 存放测试报告的路径
report_xpath = os.path.join(os.getcwd(), 'reports')
print(report_xpath)

# 报告文件
now_date = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
report_file = os.path.join(report_xpath + '\\' + now_date + 'result.html')
print(report_file)

discover = unittest.defaultTestLoader.discover(start_dir=run_xpath,
                                               pattern='wechat_access_token.py')

if __name__ == "__main__":
    with open(file=report_file, mode='ab+') as f:
        runner = BSTestRunner(
            stream=f,
            title='接口自动化测试报告',
            description='运行环境：window10\\Python\\unittest\\Excel'
        )
        runner.run(discover)

    f.close()
    pass