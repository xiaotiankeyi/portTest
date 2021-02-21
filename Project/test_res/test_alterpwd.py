import unittest

import requests

from start import startup


class Testalterpwd(startup):
    cookies = ""

    def test_case1(self):
        """设置支付密码失败,密码不一致"""
        row = 3
        global cookies
        cookies = cookies

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = requests.request(
            method=self.obj.get_value(
                row,
                self.obj.get_method()),
            url=url,
            data=data,
            cookies=cookies)

        assert self.obj.get_value(row, self.obj.get_verifyID()) in obj.text

    def test_case2(self):
        """设置支付密码失败,请输入新密码"""
        row = 4

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = requests.request(
            method=self.obj.get_value(
                row,
                self.obj.get_method()),
            url=url,
            data=data,
            cookies=cookies)

        assert self.obj.get_value(row, self.obj.get_verifyID()) in obj.text

    def test_case3(self):
        """设置支付密码失败,请确认新密码"""
        row = 5

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = requests.request(
            method=self.obj.get_value(
                row,
                self.obj.get_method()),
            url=url,
            data=data,
            cookies=cookies)

        assert self.obj.get_value(row, self.obj.get_verifyID()) in obj.text

    def test_case4(self):
        """设置支付密码失败,请输入新密码"""
        row = 6

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = requests.request(
            method=self.obj.get_value(
                row,
                self.obj.get_method()),
            url=url,
            data=data,
            cookies=cookies)

        assert self.obj.get_value(row, self.obj.get_verifyID()) in obj.text

    def test_case5(self):
        """设置支付密码成功"""
        row = 7

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = requests.request(
            method=self.obj.get_value(
                row,
                self.obj.get_method()),
            url=url,
            data=data,
            cookies=cookies)

        assert self.obj.get_value(row, self.obj.get_verifyID()) in obj.text


if __name__ == "__main__":
    unittest.main()
