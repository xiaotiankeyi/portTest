import requests
import json
from requests_toolbelt import MultipartEncoder


def A():
    url = "http://192.168.1.125/20191020bjl_app/app/base/settle_index/login"

    m = MultipartEncoder(
        fields={
            'username': '18888888888',
            'password': 'a123456'
        }
    )

    response = requests.request(method='post', url=url,
                                verify=False, data=m, headers={'Content-Type': m.content_type})
    #获取cookies
    a = requests.utils.dict_from_cookiejar(response.cookies)

    return a
    # js = response.json()
    # print(js["msg"], js['data']['key'], js['data']['token'])

def B(cookies):
    """查看实名认证信息"""
    url2 = 'http://192.168.1.125/20191020bjl_app/app/identity/settle_identity/index'
    response2 = requests.request(method='get', url=url2, cookies=cookies)

    print(response2.text)

def C(cookies):
    """查看登录信息"""
    url3 = 'http://192.168.1.125/20191020bjl_app/app/user/settle_user/info'
    response3 = requests.request(method='get', url=url3, cookies=cookies)
    print(response3.text)

def D(cookies):
    """修改会员信息"""
    url4 = 'http://192.168.1.125/20191020bjl_app/app/user/settle_user/setnickname'
    data = {
        'nickname':'赖敏'
    }
    response4 = requests.request(method='post', url=url4, cookies=cookies, data=data)
    print(response4.text)

def E(cookies):
    """设置支付密码"""
    url4 = 'http://192.168.1.125/20191020bjl_app/app/user/settle_user/setsecpwd'
    data = {
        'pwd':'123456',
        'repwd':'123456'
    }
    response5 = requests.request(method='post', url=url4, cookies=cookies, data=data)
    print(response5.text)

if __name__ == "__main__":
    cookies = A()
    B(cookies)
    D(cookies)
    C(cookies)
    E(cookies)

