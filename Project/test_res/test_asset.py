import unittest

from requestway import RunMain
from start import startup


class Testaset(startup):
    cookies = ""

    def test_case1(self):
        """查看金豆资产信息"""
        row = 8
        global cookies
        cookies = self.cookies
        url = self.obj.get_value(row, self.obj.get_host()) + self.obj.get_value(row, self.obj.get_urlxpath())  # 读取url
        method = self.obj.get_value(row, self.obj.get_method())  # 读取请求方式
        data = eval(self.obj.get_value(row, self.obj.get_params()))  # 读取数据

        target = RunMain()
        returnData = target.run_main(url=url, method=method, data=data, cookies=cookies)

        self.assertIn(self.obj.get_value(row, self.obj.get_verifyID()), returnData)  # 读取断言数据

    # @unittest.skip(reason="不测试")
    def test_case2(self):
        """查看红豆资产信息"""
        row = 9

        url = self.obj.get_value(row, self.obj.get_host()) + self.obj.get_value(row, self.obj.get_urlxpath())  # 读取url
        method = self.obj.get_value(row, self.obj.get_method())  # 读取请求方式
        data = eval(self.obj.get_value(row, self.obj.get_params()))  # 读取数据

        target = RunMain()
        returnData = target.run_main(url=url, method=method, data=data, cookies=cookies)

        self.assertIn(self.obj.get_value(row, self.obj.get_verifyID()), returnData)  # 读取断言数据

    # @unittest.skip(reason='暂停')
    def test_case3(self):
        """查看产品劵资产信息"""
        row = 10

        url = self.obj.get_value(row, self.obj.get_host()) + self.obj.get_value(row, self.obj.get_urlxpath())  # 读取url
        method = self.obj.get_value(row, self.obj.get_method())  # 读取请求方式
        data = eval(self.obj.get_value(row, self.obj.get_params()))  # 读取数据

        target = RunMain()
        returnData = target.run_main(url=url, method=method, data=data, cookies=cookies)

        self.assertIn(self.obj.get_value(row, self.obj.get_verifyID()), returnData)  # 读取断言数据

    # @unittest.skip(reason="不测试")
    def test_case4(self):
        """查看产品卷资产信息"""
        row = 11

        url = self.obj.get_value(row, self.obj.get_host()) + self.obj.get_value(row, self.obj.get_urlxpath())  # 读取url
        method = self.obj.get_value(row, self.obj.get_method())  # 读取请求方式
        data = eval(self.obj.get_value(row, self.obj.get_params()))  # 读取数据

        target = RunMain()
        returnData = target.run_main(url=url, method=method, data=data, cookies=cookies)

        self.assertIn(self.obj.get_value(row, self.obj.get_verifyID()), returnData)  # 读取断言数据


if __name__ == "__main__":
    unittest.main()
