import unittest

from requestway import RunMain
from showDatabase import mysql
from start import startup


class Testshopping(startup):
    cookies = ""
    commodity = ""

    def test_case1(self):
        """查看购物车数据"""
        global cookies
        cookies = self.cookies
        row = 19

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

    def test_case2(self):
        """购物车添加商品成功"""
        row = 20
        # 查看商品列表,获取商品id
        sql = "SELECT id,shop_goods_class_id,goods_name from ds_settle_shop_goods;"
        value = mysql(sql=sql, way='select')

        url = self.obj.get_value(row,
                                 self.obj.get_host()) + self.obj.get_value(row,
                                                                           self.obj.get_urlxpath())
        method = self.obj.get_value(row, self.obj.get_method())
        data = eval(self.obj.get_value(row, self.obj.get_params()))
        data['goodsid'] = value['id']

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

        sql = "SELECT * from ds_settle_shop_cart WHERE user_id=1;"
        data = mysql(sql=sql, way='select')
        if data is not None:
            global commodity
            commodity = data['shop_goods_id']


if __name__ == "__main__":
    unittest.main()
