import unittest

from requestway import RunMain
from showDatabase import mysql
from start import startup


class Testaddress(startup):
    addressID = ""
    cookies = ""

    def test_case1(self):
        """添加收获地址失败,手机号码错误"""
        row = 12
        global cookies      #设置为全局
        cookies = self.cookies

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = eval(
            self.obj.get_value(
                row,
                self.obj.get_params()))  # 记得用eval函数转化为字典

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

    # @unittest.skip(reason='测试')
    def test_case2(self):
        """添加收获地址失败,联系人输入框为空"""
        row = 13

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = eval(self.obj.get_value(row, self.obj.get_params()))

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

    # @unittest.skip(reason='不测试')
    def test_case3(self):
        """添加收获地址成功"""
        row = 14

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = eval(
            self.obj.get_value(
                row,
                self.obj.get_params()))  # 记得用eval函数转化为字典

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

        # 数据库查询,获取地址id,并转化为全局变量
        sql = 'SELECT * from ds_settle_user_address WHERE user_id=1;'
        mysqldata = mysql(sql=sql, way='select')
        if mysqldata is not None:
            global addressID
            addressID = mysqldata['id']  # 获取收获地址ID,转化为全局变量
        else:
            raise NameError("查询数据为空")

    # @unittest.skip(reason='不测试')
    def test_case4(self):
        """查询收货地址"""
        row = 15

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = {"id": addressID}  # 引入收货地址id

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

    # @unittest.skip(reason='不测试')
    def test_case5(self):
        """修改收货地址"""
        row = 16

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = eval(
            self.obj.get_value(
                row,
                self.obj.get_params()))  # 记得用eval函数转化为字典
        data['id'] = addressID  # 改变 收货地址id

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

        # 数据库查询,获取地址id,并转化为全局变量
        sql = 'SELECT * from ds_settle_user_address WHERE user_id=1;'
        mysqldata = mysql(sql=sql, way='select')

        if mysqldata is not None:
            if mysqldata['realname'] == '黄晶':
                pass
        else:
            raise NameError("添加失敗")

    # @unittest.skip(reason='不测试')
    def test_case6(self):
        """删除收货地址"""
        row = 17

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = {"id": addressID}  # 记得用eval函数转化为字典

        obj = RunMain()
        returnvalue = obj.run_main(
            url=url,
            method=method,
            data=data,
            cookies=cookies)

        self.assertIn(
            self.obj.get_value(
                row,
                self.obj.get_verifyID()),
            returnvalue)

        # 数据库查询,获取地址id,并转化为全局变量
        sql = 'SELECT * from ds_settle_user_address WHERE user_id=1;'
        mysqldata = mysql(sql=sql, way='select')
        if mysqldata is not None:
            pass
        else:
            pass


if __name__ == "__main__":
    unittest.main()
