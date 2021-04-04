from pytest_project.public.base_module import *
from pytest_project.public.excelData import accept


# ('Y', 'http://127.0.0.1:7777/login/', 'POST', {'Content-Type': 'application/json'}, '{"username": "", "password": 123456}', '用户名不能为空')
# 简化了excel数据读取的步骤

class Testlogin(startup):

    def test_case_01(self, base_url):
        requestData = accept(row=1, sheet_name='登录')

        # print(requestData[3], type(requestData[3]))
        # print(requestData[1])
        if requestData[0] == 'Y':
            response = request.run_main(url=base_url + requestData[1], method=requestData[2],
                                        headers=requestData[3], data=requestData[4])
            print(response)
            assert requestData[5] == response['msg']
            logger.info("{}请求成功,body响应{}".format(requestData[1], response))
        else:
            print('不执行')
            pass

    def test_case_02(self, base_url):
        requestData = accept(row=2, sheet_name='登录')

        # print(requestData[3], type(requestData[3]))
        # print(requestData[1])
        if requestData[0] == 'Y':
            response = request.run_main(url=base_url + requestData[1], method=requestData[2],
                                        headers=requestData[3], data=requestData[4])
            print(response)
            assert requestData[5] == response['msg']
            logger.info("{}请求成功,body响应{}".format(requestData[1], response))
        else:
            print('不执行')
            pass


if __name__ == "__main__":
    pytest.main(['-vs', 'test_loginTest.py::Testlogin'])
