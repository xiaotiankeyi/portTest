import os
import unittest

import ddt
import requests
from requests_toolbelt import MultipartEncoder

from start import startup


@ddt.ddt
class Testlogin(startup):

    def loginfunc(self, key, key2, key3, key4, num):
        """登录成功"""
        row1 = num

        url = self.obj.get_value(row1,
                                 self.obj.get_host()) + self.obj.get_value(row1,
                                                                           self.obj.get_urlxpath())

        # m = MultipartEncoder(
        # fields=eval(self.obj.get_value(row1, self.obj.get_params())))  #
        # 获取需要发送的数据
        m = MultipartEncoder(
            fields={key: key2, key3: key4})

        response = requests.request(
            method=self.obj.get_value(
                row1,
                self.obj.get_method()),
            url=url,
            verify=False,
            data=m,
            headers={
                'Content-Type': m.content_type})

        assert self.obj.get_value(
            row1, self.obj.get_verifyID()) in response.text  # 获取预期判断值

    @ddt.file_data(
        os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))) +
            '\\public' +
            '\\test_data' +
            '\\user.json'))
    def test_data(self, key, key2, key3, key4, num):
        self.loginfunc(key, key2, key3, key4, num)

    @unittest.skip(reason='不测试')
    def test_case2(self):
        """登录失败"""
        row2 = 2

        url = self.obj.get_value(row2,
                                 self.obj.get_host()) + self.obj.get_value(row2,
                                                                           self.obj.get_urlxpath())

        m = MultipartEncoder(
            fields=eval(
                self.obj.get_value(
                    row2,
                    self.obj.get_params())))  # 获取需要发送的数据

        response = requests.request(
            method=self.obj.get_value(
                row2,
                self.obj.get_method()),
            url=url,
            verify=False,
            data=m,
            headers={
                'Content-Type': m.content_type})

        assert self.obj.get_value(
            row2, self.obj.get_verifyID()) in response.text  # 获取预期判断值


if __name__ == "__main__":
    unittest.main()
