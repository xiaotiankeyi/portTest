import requests
from requests_toolbelt import MultipartEncoder
from ReadExcel import HandleExcel


def login():
    """登录成功"""
    obj = HandleExcel()

    row1 = 1

    url = obj.get_value(row1, obj.get_host()) + obj.get_value(row1, obj.get_urlxpath())

    m = MultipartEncoder(
        fields=eval(obj.get_value(row1, obj.get_params()))        #获取需要发送的数据
    )

    response = requests.request(method=obj.get_value(row1, obj.get_method()), url=url,
                                verify=False, data=m, headers={'Content-Type': m.content_type})

    assert obj.get_value(row1, obj.get_verifyID()) in response.text            #获取预期判断值
    a = requests.utils.dict_from_cookiejar(response.cookies)        #获取cookie并返回
    return a