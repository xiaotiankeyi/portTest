import os

import requests
import urllib3
import yaml

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_path = os.path.join(base_path + '/data/' + 'yaml_Configdata.yaml')


def add_yaml_data(key, value):
    public = {key: value}

    with open(file=yaml_path, mode='a', encoding='utf-8') as f:
        yaml.dump(public, f, allow_unicode=True)

        f.close()


def rand_yaml_data(key=None):
    """
    读取
    :return:
    """
    with open(file=yaml_path, mode='r', encoding='utf-8') as f:
        data = yaml.load(f)
        # print(type(data), data[key])
        f.close()
        return data[key]


def login_token():
    """
    登录账号获取access_token在保存
    :return:
    """
    corpid = rand_yaml_data('corpid')
    # print(corpid)

    corpsecret = rand_yaml_data('corpsecret')
    # print(corpsecret)

    host = rand_yaml_data('host')
    # print(host)

    url = "%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (host, corpid, corpsecret)
    # print(url)

    response = requests.request(url=url, method='GET', data=None)

    js_data = response.json()

    # print(js_data['access_token'])

    add_yaml_data(key='access_token', value=js_data['access_token'])

    return response.json()


if __name__ == "__main__":
    # add_yaml_data(key='mysql', value=3306)
    a = rand_yaml_data(key='host')
    print(a)
    # d = login_token()
    # print(d)
    pass
