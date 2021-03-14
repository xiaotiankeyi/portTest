import json

import requests

class RunMain():

    def send_get(self, url, data, headers, cookies):
        """封装get请求方式"""
        res = requests.get(
            url=url,
            params=data,
            headers=headers,
            timeout=10,
            cookies=cookies)
        result = res.json()
        return result
        # return json.dumps(
        #     result,                   #处理返回数据
        #     indent=2,
        #     sort_keys=False,
        #     ensure_ascii=False)

    def send_post(self, url, data, headers, cookies):
        """封装port请求方法"""
        Ares = requests.post(
            url=url,
            data=data,
            headers=headers,
            timeout=10,
            cookies=cookies)
        result = Ares.json()
        return result
        # return json.dumps(
        #     result,
        #     indent=2,             #处理返回数据
        #     sort_keys=False,
        #     ensure_ascii=False)

    def run_main(self, url, method, data=None, headers=None, cookies=None):

        if method == 'GET':
            res = self.send_get(url, data, headers, cookies)
            return res
        elif method == 'POST':
            res = self.send_post(url, data, headers, cookies)
            return res


if __name__ == "__main__":
    # url = "https://www.v2ex.com/api/nodes/show.json?name=python"

    # test = RunMain()
    # print(test.run_main(url, 'GET', ))
    pass