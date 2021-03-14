from pytest_project.public.base_module import *
from pytest_project.public.readExcel import HandleExcel


@allure.feature("测试登录场景")   #描述被测试产品需求
class Testlogin(startup):
    obj = HandleExcel()

    # @allure.step('登录失败用户名为空')  # 模块下的具体步骤，使测试用例在allure报告中能够更加详细的显示测试过程
    # @allure.story("登录失败")      #用于描述feature的用户场景，即测试需求分支功能
    @allure.title("登录失败用户名为空")
    def test_case_01(self, base_url):
        """测试用户登录失败场景之用户名为空"""
        row = 1
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
            # allure.attach("断言成功,测试通过....",
            #               attachment_type=allure.attachment_type.PNG)  # allure.attach可以给报告中添加文件，图片，log，html代码等等
            # with allure.step('response %s' % response):   #指定步骤
            #     allure.description(response)
        else:
            print('不执行')
            pass

    @allure.title("登录失败用户名不存在")
    def test_case_02(self, base_url):
        """登录失败用户名不存在"""
        row = 2
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

    @allure.title("用户登录失败之密码错误")
    def test_case_03(self, base_url):
        """登录场景失败,用户名密码错误"""
        row = 3
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

    @allure.title("用户登录成功")     #可以重命名测试用例在allure报告中的名称
    def test_case_04(self, base_url):
        row = 4
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
            add_yaml_data(file=test_data_path, key='tonke', values=response['tonke'])
        else:
            print('不执行')
            pass


if __name__ == "__main__":
    pytest.main(['-vs', 'test_login.py'])

    # pytest -s -q --alluredir report生成allure报告数据
    # allure generate --clean report/ -o report_result/html把allure数据转化为html报告
