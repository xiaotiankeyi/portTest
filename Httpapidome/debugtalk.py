import time
import requests
from httprunner import __version__

from requests_toolbelt import MultipartEncoder
def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def login():
    """登录成功"""
    url = "http://127.0.0.1:7777/login/"

    m = MultipartEncoder(
        fields=
            {
                "username": "jack",
                "password": "123456"}       #获取需要发送的数据
    )

    # response = requests.request(method='post', url=url,
    #                             verify=False, data=m, headers={'Content-Type': m.content_type})

    # a = response.text        #获取cookie并返回
    # return a

if __name__ == "__main__":
    pass
    # print(login())