# import allure

class startup():

    def setup_class(self):
        print("模块级别测试环境准备 test start")

    # def setup(self):
    #     print("函数级别测试环境准备 test start")
    #
    # def teardown(self):
    #     print("函数级别测试环境准备 test stop")

    def teardown_class(self):
        print("模块级别测试结束 test stop")