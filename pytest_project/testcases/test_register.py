from pytest_project.public.base_module import *
from pytest_project.public.readExcel import HandleExcel

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

if __name__ == "__main__":
    pytest.main(['-vs', 'test_register.py::Testregister::test_case_01'])