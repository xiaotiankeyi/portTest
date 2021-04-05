from pytest_project.public.base_module import *
from pytest_project.public.readExcel import HandleExcel
from pytest_project.public.yamlData import accept


@allure.feature("注册模块功能")
class Testregister(startup):
    obj = HandleExcel(sheet_name='接口测试')

    @allure.story("注册失败")
    @allure.title("注册失败之用户以存在")
    def test_case_01(self, base_url):
        row = 5
        yn = self.obj.get_value(row, self.obj.get_YN())
        url = base_url + self.obj.get_value(row, self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        headers = eval(self.obj.get_value(row, self.obj.get_headers()))
        data = eval(self.obj.get_value(row, self.obj.get_data()))
        data = json.dumps(data)
        assert_val = self.obj.get_value(row, self.obj.get_assert())

        if yn == 'Y':
            response = request.run_main(url=url, method=method, headers=headers, data=data)
            print(response)
            assert assert_val == response['msg']
        else:
            print('不执行')
            pass

    def test_case_02(self, base_url):
        val = accept(file=testapi_data_path, file_name='register_test.yaml', key='teststeps3')
        # print(val['name'])
        # print(val['request']['headers'])
        # print(val['request']['json'])
        data = json.dumps(val['request']['json'])

        response = request.run_main(url=base_url+val['request']['url'],
                                    method=val['request']['method'],
                                    headers=val['request']['headers'],
                                    data=data)
        print(response)
        assert val['validate']['msg'] == response['msg']
        assert val['validate']['msg_code'] == response['msg_code']


if __name__ == "__main__":
    pytest.main(['-vs', 'test_register.py::Testregister::test_case_02'])